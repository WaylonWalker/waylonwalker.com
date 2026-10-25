#!/usr/bin/env node
// Fast source-level guard for the published sample page. It does NOT replace a browser render check.
// Mermaid 10.9.5 is deployed today; avoid fixtures that require Mermaid 11.
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, resolve } from "node:path";

function audit(source){
 const failures=[];const diagramBlocks=[];const containers=[];let fence=null;
 const lines=source.split(/\r?\n/);
 for(let i=0;i<lines.length;i++){
  const line=lines[i],lineNo=i+1;
  const f=line.match(/^\s*(`{3,})([^`]*)$/);
  if(f){
   const width=f[1].length,info=f[2].trim().toLowerCase();
   if(!fence){fence={width,language:info.split(/\s+/)[0],start:lineNo,lines:[]};continue}
   if(width>=fence.width&&info===""){if(fence.language==="mermaid")diagramBlocks.push({...fence,source:fence.lines.join("\n")});fence=null;continue}
  }
  if(fence){fence.lines.push(line);continue}
  const stripped=line.trim();
  if(/^:{3,}\s+\S/.test(stripped)){
    const depth=stripped.match(/^:+/)[0].length;
    if(containers.length&&depth<=containers.at(-1).depth)failures.push(`line ${lineNo}: nested container must use more colons than its parent`);
    containers.push({depth,lineNo});
  }else if(/^:{3,}$/.test(stripped)){
    if(!containers.length){failures.push(`line ${lineNo}: unmatched container closing fence`);continue}
    const top=containers.pop();
    if(top.depth!==stripped.length)failures.push(`line ${lineNo}: expected ${top.depth} colons to close container from line ${top.lineNo}`);
    const nextLine = lines[i + 1]?.trim() ?? "";
    const nextClose = nextLine.match(/^(:{3,})$/);
    if (containers.length && nextClose && nextClose[1].length < top.depth) {
     failures.push(`line ${lineNo+1}: separate nested and parent closing fences with a blank line to keep the nested content boundary intact`);
    }
  }
 }
 if(fence)failures.push(`line ${fence.start}: unclosed Markdown code fence`);
 for(const item of containers)failures.push(`line ${item.lineNo}: unclosed Markdown container`);
 if(diagramBlocks.length<10)failures.push(`expected a gallery of at least 10 rendered Mermaid diagrams; got ${diagramBlocks.length}`);
 for(const diagram of diagramBlocks){
  const source=diagram.source.replace(/^\s*---\s*\n[\s\S]*?\n---\s*\n/,"").trim();
  const type=source.split(/\r?\n/,1)[0].trim();
  if(!/^(flowchart\b|graph\b|gitGraph\b|xychart-beta\b|mindmap\b|stateDiagram-v2\b|journey\b|timeline\b)/.test(type))failures.push(`line ${diagram.start}: unknown/unsupported Mermaid diagram type ${JSON.stringify(type)}`);
  if(/^gitGraph:/.test(type)||/^architecture-beta/.test(type)||(/^\s*rebase\s*$/m.test(source)&&/^gitGraph/.test(type)))failures.push(`line ${diagram.start}: Mermaid 10 incompatible diagram syntax`);
 }
 return {diagrams:diagramBlocks.length,failures};
}

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const file = resolve(root, "pages/sample.md");
const report = audit(readFileSync(file, "utf8"));
if (report.failures.length) {
  for (const failure of report.failures) console.error(failure);
  process.exitCode = 1;
} else {
  console.log("Sample fixture: " + report.diagrams + " Mermaid diagrams and balanced containers");
}
