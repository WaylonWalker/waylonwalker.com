---
date: <% tp.date.now("YYYY-MM-DD HH:mm:ss") %>
templateKey: gratitude
published: true
tags:
- gratitude
<%*
const folder = "pages/gratitude";

// get all files in the vault, keep only those inside the folder
const files = app.vault.getFiles().filter(f => f.path.startsWith(folder + "/"));

// extract numeric suffixes from filenames like gratitude-123.md
const nums = files.map(f => {
  const m = f.basename.match(/^gratitude-(\d+)$/);
  return m ? parseInt(m[1], 10) : null;
}).filter(n => n !== null);

// next number (start at 1 if none exist)
const next = (nums.length ? Math.max(...nums) : 0) + 1;

// include the .md extension when moving
const newPath = `${folder}/gratitude-${next}`;
await tp.file.move(newPath);
%>
---
