---
date: 2025-12-13 22:28:28
templateKey: til
title: numbered posts in obsidian
published: true
tags:
  - obsidian

---

I've been using this one for awhile now, I have a post type that I only edit
from my phone, but I have all the post numbered.  I set up a template in
obsidian for using templater, the template goes right in the static site repo,
I point templater to the templates directory and this has been working pretty
seamlessly for awhile.

``` md
---
date: <% tp.date.now("YYYY-MM-DD HH:mm:ss") %>
templateKey: myposttype
published: true
tags:
- myposttype
<%*
const folder = "pages/myposttype";

// get all files in the vault, keep only those inside the folder
const files = app.vault.getFiles().filter(f => f.path.startsWith(folder + "/"));

// extract numeric suffixes from filenames like myposttype-123.md
const nums = files.map(f => {
  const m = f.basename.match(/^myposttype-(\d+)$/);
  return m ? parseInt(m[1], 10) : null;
}).filter(n => n !== null);

// next number (start at 1 if none exist)
const next = (nums.length ? Math.max(...nums) : 0) + 1;

// include the .md extension when moving
const newPath = `${folder}/myposttype-${next}`;
await tp.file.move(newPath);
%>
---
```
