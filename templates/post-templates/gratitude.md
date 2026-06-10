---
date: <% tp.date.now("YYYY-MM-DD HH:mm:ss") %>
templateKey: gratitude
published: true
tags:
- gratitude
<%*
const folder = "pages/gratitude";

// Find existing gratitude posts and assign the next number.
const files = app.vault.getFiles().filter(f => f.path.startsWith(folder + "/"));

const nums = files.map(f => {
  const m = f.basename.match(/^gratitude-(\d+)$/);
  return m ? parseInt(m[1], 10) : null;
}).filter(n => n !== null);

const next = (nums.length ? Math.max(...nums) : 0) + 1;
const newPath = `${folder}/gratitude-${next}`;
await tp.file.move(newPath);
%>
---
