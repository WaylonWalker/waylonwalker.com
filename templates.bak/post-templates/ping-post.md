---
date: <% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>
templateKey: ping
title: <%*
  const originalFileName = await tp.system.prompt("Enter file name");
  const toTitleCase = str => str.replace(
    /\w\S*/g,
    txt => txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase()
  );
  const title = toTitleCase(originalFileName);
  tR += title + '\n'; // Add the title to the template result
-%>
published: true
tags:
  - ping
---
<%*
const folder = "pages/ping";

// get all files in the vault, keep only those inside the folder
const files = app.vault.getFiles().filter(f => f.path.startsWith(folder + "/"));

// extract numeric suffixes from filenames like ping-123.md
const nums = files.map(f => {
  const m = f.basename.match(/^ping-(\d+)$/);
  return m ? parseInt(m[1], 10) : null;
}).filter(n => n !== null);

// next number (start at 1 if none exist)
const next = (nums.length ? Math.max(...nums) : 0) + 1;

// include the .md extension when moving
const newPath = `${folder}/ping-${next}`;
await tp.file.move(newPath);
%>
