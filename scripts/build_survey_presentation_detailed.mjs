import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath, pathToFileURL} from 'node:url';
import {createRequire} from 'node:module';
import {Presentation, PresentationFile, FileBlob} from '@oai/artifact-tool';
const {Canvas}=createRequire(import.meta.resolve('@oai/artifact-tool'))('skia-canvas');
import {slides as mainSlides, rosterTopics} from './survey_presentation_content.mjs';

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const work=path.join(root,'.survey_work/presentation-detailed');
const output=path.join(root,'presentations');
const skill=process.env.SURVEY_PRESENTATION_SKILL || 'D:/DevData/Codex/plugins/cache/openai-primary-runtime/presentations/26.1026.10807/skills/presentations';
const python=process.env.SURVEY_PYTHON || 'C:/Users/89447/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe';
process.env.RUNTIME_NODE_MODULES ??= 'C:/Users/89447/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules';
const {finalizePresentation}=await import(pathToFileURL(path.join(skill,'container_tools/artifact_tool_utils.mjs')));
await fs.mkdir(work,{recursive:true}); await fs.mkdir(output,{recursive:true});
const survey=JSON.parse(await fs.readFile(path.join(root,'data/benchmark_survey.json'),'utf8'));
const sourceData=JSON.parse(await fs.readFile(path.join(root,'data/benchmark_reading_sources.json'),'utf8'));
const entries=new Map(survey.entries.map(e=>[e.name,e]));
const sources=new Map(sourceData.entries.map(e=>[e.benchmark,e]));
const active=survey.entries.filter(e=>e.focus==='active');
for(const e of active)if(!rosterTopics[e.name])throw new Error(`Missing precise appendix topic: ${e.name}`);
const revisions={
  'LIBERO-Safety':{
    results:'论文表 3 中 OpenVLA-OFT 在 AAG 的 L0／L1／L2 安全约束任务成功率为 50.0%／79.3%／1.3%。物理安全轨的 SR 要求完成任务且全程无约束违规；任一次违规即终止并记失败。',
    limits:'SR 已包含安全约束，不能把它解释为与安全无关的普通任务完成率。难度之间的训练覆盖不同；部分组件公开状态仍需按代码审计确认。',
    metrics:'物理安全轨 SR：完成任务且全程无安全约束违规的测试试验比例；SSR：Semantic Safety Reasoning 语义安全推理套件，并非 SafeStage 的安全成功率。'
  },
  'DESPITE':{
    results:'Gemini-3-Pro-Preview 在 1,044 个困难任务上未生成有效计划的比例为 0.4%；危险计划比例在摘要为 28.3%，在正文 §1.1 为 28.7%，两处存在不一致，故本汇报概括为约 28%。18 个开源模型的规模分析须与该模型结果分别解释。'
  }
};
const types={benchmark:'评测任务集',dataset:'训练数据集',platform:'仿真平台',framework:'评测框架',method:'方法论文'};
const FONT='Microsoft YaHei';
const p=Presentation.create({slideSize:{width:1440,height:810}});p.theme.defaultFont=FONT;
const references=[];const tableOwners=[];const metrics=[];const outline=[];
const ctx=new Canvas(100,100).getContext('2d');
const widthOf=(t,size,bold=false)=>{ctx.font=`${bold?'bold ':''}${size}px "${FONT}"`;return ctx.measureText(t).width;};
function wrap(t,width,size,bold=false){
  const lines=[];
  for(const paragraph of String(t).split('\n')){
    if(!paragraph){lines.push('');continue;}
    const raw=paragraph.match(/[A-Za-z0-9@][A-Za-z0-9@._/,+%→-]*|[^A-Za-z0-9@]/gu)||[];
    const tokens=[];
    let pending='';
    for(const token of raw){
      if(/^[（(《“‘【]$/u.test(token)){pending+=token;continue;}
      if(/^[，。；：？！、）)》”’】%]$/u.test(token)&&tokens.length){tokens[tokens.length-1]+=token;continue;}
      const word=pending+token;pending='';
      if(widthOf(word,size,bold)>width-4&&word.includes('-')){
        tokens.push(...word.match(/[^-]+-?|-/g));
      }else tokens.push(word);
    }
    if(pending)tokens.push(pending);
    let line='';
    for(const token of tokens){
      if(widthOf(line+token,size,bold)>width-8 && line){lines.push(line.trimEnd());line=token.trimStart();}
      else line+=token;
    }
    if(line)lines.push(line.trimEnd());
  }
  return lines;
}
function text(s,t,x,y,w,h,size=23,bold=false,color='#171717'){
  const box=s.shapes.add({geometry:'textbox',position:{left:x,top:y,width:w,height:h},fill:'none',line:{fill:'none',width:0}});
  box.text=String(t);box.text.style={typeface:FONT,fontSize:size,bold,color,wrap:'none',autoFit:'none',verticalAlignment:'top',insets:0};
  return box;
}
function block(s,t,y,size=23,bold=false,color='#171717',x=55,w=1330){
  const lines=wrap(t,w,size,bold);const h=lines.length*size*1.28+4;
  text(s,lines.join('\n'),x,y,w,h,size,bold,color);return h;
}
function getRef(name){if(!references.includes(name))references.push(name);return references.indexOf(name)+1;}
function sourceNotes(names){
  return names.map(name=>{
    const src=sources.get(name),e=entries.get(name);
    if(!src||!e)throw new Error(`Unknown source ${name}`);
    const revised=revisions[name]||{};
    return `[${getRef(name)}] ${src.metadata.authors.join(', ')}. ${src.metadata.title}. arXiv:${src.metadata.version}. ${src.fulltext_url}\n核查章节：${e.evidence.classification_basis.sections.join('；')}\n论文结果：${revised.results||e.summary.results}\n结果边界：${revised.limits||e.summary.limits}\n引用记录：${e.citation.cited_by_count??'未知'}；${e.citation.snapshot_date??'未记录'}；${e.citation.openalex_id??''}\n项目入口：${e.resources.urls.join('；')}\n本地：benchmarks/${e.document}`;
  }).join('\n\n');
}
function base(d){
  const s=p.slides.add();s.background.fill='#FFFFFF';
  const n=p.slides.items.length;const refs=(d.refs||[]).map(getRef);
  block(s,d.title,28,d.kind==='cover'?42:35,true);
  text(s,String(n).padStart(2,'0'),1335,777,50,23,15,false,'#555555');
  const footer=refs.length?`来源：${refs.map(n=>`[${n}]`).join(' ')}。论文版本与核查位置见备注。`:'来源：本仓库 2026-11-03 调研资料。具体文件见备注。';
  text(s,footer,55,777,1260,23,14,false,'#555555');
  s.speakerNotes.text=[d.note||'', '资料快照：2026-11-03。文中试验结果来自原论文，未由本项目运行复现。',
    ...(d.local||[]).map(x=>`本地来源：${x}`),sourceNotes(d.refs||[])].filter(Boolean).join('\n\n');
  outline.push({...d,number:n});return s;
}
function tableLayout(headers,rows,widths,size){
  const values=[headers,...rows].map((row,r)=>row.map((v,c)=>wrap(v,widths[c]-24,size,r===0).join('\n')));
  const heights=values.map((row,r)=>Math.max(...row.map(v=>v.split('\n').length)) * size*1.23+15+(r===0?2:0));
  return {values,heights,h:heights.reduce((a,b)=>a+b,0)};
}
function nativeTable(s,headers,rows,widths,y,available,font=23,min=20){
  let size=font,layout=tableLayout(headers,rows,widths,size);
  while(layout.h>available&&size>min){size-=0.5;layout=tableLayout(headers,rows,widths,size);}
  if(layout.h>available+1)throw new Error(`Slide ${p.slides.items.length} table needs ${layout.h.toFixed(0)}px but has ${available.toFixed(0)}px at ${size}px`);
  const t=s.tables.add({rows:rows.length+1,columns:headers.length,left:55,top:y,width:1330,height:layout.h,columnWidths:widths,values:layout.values});
  t.styleOptions={headerRow:false,bandedRows:false};
  t.borders.assign({fill:'#B9B9B9',width:0.6,style:'solid'});
  t.cells.block({row:0,column:0,rowCount:rows.length+1,columnCount:headers.length}).assign({textStyle:{typeface:FONT,fontSize:size,color:'#171717'},margins:{top:5,right:11,bottom:5,left:11},anchor:'center'});
  for(let r=0;r<layout.values.length;r++){
    t.rows[r].height=layout.heights[r];
    for(let c=0;c<headers.length;c++){
      const cell=t.getCell(r,c);cell.fill=r===0?'#E8E8E8':'#FFFFFF';
      cell.text.style={typeface:FONT,fontSize:size,color:'#171717',bold:r===0,insets:5,verticalAlignment:'middle',autoFit:'none'};
    }
  }
  tableOwners.push(p.slides.items.length);metrics.push({slide:p.slides.items.length,fontSize:size,tableHeight:layout.h,available});
  return layout.h;
}
function compose(d){
  const s=base(d);let y=95;
  if(d.kind==='cover'){
    y=155; y+=block(s,d.subtitle,y,29,true)+70;
    for(const paragraph of d.paragraphs){y+=block(s,paragraph,y,26)+25;}
    block(s,d.takeaway,685,21,false,'#444444');return;
  }
  if(d.lead)y+=block(s,d.lead,y,22.5)+17;
  const paragraphs=d.paragraphs||[];
  const paraSize=22.5;
  const reserve=paragraphs.reduce((a,t)=>a+wrap(t,1330,paraSize).length*paraSize*1.28+4+12,0)
    +(d.takeaway?wrap(d.takeaway,1330,21.5).length*21.5*1.28+4+14:0);
  if(d.headers)y+=nativeTable(s,d.headers,d.rows,d.widths,y,755-y-reserve-14,d.font??23,d.minFont??20)+16;
  for(const paragraph of paragraphs)y+=block(s,paragraph,y,paraSize)+12;
  if(d.takeaway){y+=3;y+=block(s,d.takeaway,y,21.5,true);}
  if(y>762)throw new Error(`Slide ${p.slides.items.length} content extends to ${y}`);
}

for(const source of mainSlides){
  const d=structuredClone(source);
  if(d.kind==='citations'){
    d.headers=['来源论文示例','OpenAlex 被引观测','观测日期'];d.widths=[650,330,350];
    d.rows=d.names.map(n=>[n,String(entries.get(n).citation.cited_by_count),entries.get(n).citation.snapshot_date]);
    d.note=(d.note||'')+'\n'+d.names.map(n=>`${n}：${entries.get(n).citation.openalex_id}`).join('\n');
  }
  compose(d);
}
const mainRefNames=[...references];
for(let start=0;start<active.length;start+=8){
  const group=active.slice(start,start+8);
  const d={title:`附录 B：62 项重点研究索引（${Math.floor(start/8)+1}/8）`,
    lead:`第 ${start+1}–${start+group.length} 项。下表列出主要成果、研究目标与评测单位；episode 指一次完整测试试验。实现细节、论文结果和项目地址见备注与条目文档。`,
    headers:['条目／所读版本','主要成果','主要研究目标','评测单位'],widths:[340,150,560,280],font:21,minFont:19.5,
    rows:group.map(e=>[`${e.name}\n${e.source.version}`,types[e.primary_type],rosterTopics[e.name],e.unit]),
    refs:group.map(e=>e.name),local:['data/benchmark_survey.json'],
    note:'以下为完整索引。分类仅反映实际阅读来源的主要贡献，合并条目沿用历史身份。\n'+group.map(e=>`${e.name}：\n实现：${e.summary.implementation}\n场景：${e.summary.scenarios}\n指标：${revisions[e.name]?.metrics||e.metrics.map(m=>m.join('：')).join('；')}`).join('\n\n')};
  compose(d);
}
// Main references are displayed in full; the complete 62-source list is in roster notes.
for(let start=0;start<mainRefNames.length;start+=7){
  const names=mainRefNames.slice(start,start+7);
  const d={title:`附录 C：正文主要参考文献（${Math.floor(start/7)+1}/${Math.ceil(mainRefNames.length/7)}）`,
    lead:'以下采用实际核查的 arXiv 版本。完整作者信息与正文地址保存在讲者备注中；论文日期与任务规模均按所读版本解释。',
    headers:['编号','论文题名与来源版本'],widths:[100,1230],font:20.5,minFont:20,
    rows:names.map(name=>{const src=sources.get(name);return [`[${getRef(name)}]`,`${src.metadata.title}\narXiv:${src.metadata.version}　${src.fulltext_url}`];}),refs:names};
  compose(d);
}

await fs.writeFile(path.join(work,'outline.json'),JSON.stringify(outline,null,2));
await fs.writeFile(path.join(work,'layout-metrics.json'),JSON.stringify(metrics,null,2));
const prose=['# 具身智能及安全 Benchmark 调研汇报：详细修订稿','资料快照：2026-11-03。此文件与详细修订版 PPT 的可见文字来自同一内容源。'];
for(const d of outline){
  prose.push(`\n## ${d.number}. ${d.title}\n`,d.lead||d.subtitle||'');
  if(d.headers){prose.push(`\n| ${d.headers.join(' | ')} |`,`| ${d.headers.map(()=>'---').join(' | ')} |`);for(const row of d.rows)prose.push(`| ${row.map(v=>String(v).replaceAll('\n','<br>').replaceAll('|','／')).join(' | ')} |`);}
  if(d.paragraphs)prose.push('\n'+d.paragraphs.join('\n\n'));
  if(d.takeaway)prose.push('\n'+d.takeaway);
  if(d.refs?.length)prose.push('\n来源：'+d.refs.map(name=>{const src=sources.get(name);return `[${name}](${src.fulltext_url})`;}).join('；')+'。');
}
await fs.writeFile(path.join(output,'调研汇报_详细修订稿.md'),prose.join('\n'));
const draft=path.join(work,'candidate.pptx');
await (await PresentationFile.exportPptx(p)).save(draft);
const only=process.env.SURVEY_RENDER_SLIDES?new Set(process.env.SURVEY_RENDER_SLIDES.split(',').map(Number)):null;
for(let i=0;i<p.slides.items.length;i++){
  if(only&&!only.has(i+1))continue;
  const png=await p.export({slide:p.slides.items[i],format:'png',scale:1});
  await fs.writeFile(path.join(work,`slide-${String(i+1).padStart(2,'0')}.png`),new Uint8Array(await png.arrayBuffer()));
}
if(process.env.SURVEY_DRAFT_ONLY==='1'){
  console.log(JSON.stringify({slides:p.slides.items.length,draft,tableCount:tableOwners.length,minimumTableFont:Math.min(...metrics.map(m=>m.fontSize))}));
}else{
  const finalPath=path.join(output,process.env.SURVEY_PPTX_NAME||'具身智能及安全Benchmark调研汇报_2026-11-03_详细修订版.pptx');
  await finalizePresentation({workspaceDir:root,candidatePath:draft,finalPath,pythonExecutable:python,
    integrityValidatorPath:path.join(skill,'container_tools/inspect_presentation_package_integrity.py'),
    layoutValidatorPath:path.join(skill,'container_tools/inspect_presentation_layout_geometry.py'),
    layoutArgs:['--expected-slide-size-emu','13716000,7715250','--validate-heading-fit',...tableOwners.flatMap(n=>['--require-native-table-slide',String(n)])],
    requiredNativeTableOwnerSlides:tableOwners,requiredNativeChartOwnerSlides:[],fontPolicy:{basis:'design',families:[FONT]},verifyArtifactToolImport:true,
    receiptPath:path.join(work,`${path.basename(finalPath)}.validation.json`)});
  console.log(JSON.stringify({slides:p.slides.items.length,finalPath,finalized:true}));
}
