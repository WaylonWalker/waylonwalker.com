---
date: 2024-07-31 13:34
templateKey: til
title: Obsidian Using Templater Like Copier
published: true
tags:
  - obsidian
---

I've long used copier to create all of my posts for my blog, and it works
really well for my workflow.  I think of a title, call a template, and give it
a title.  out of the box obsidian did not seem to work this way.  It seems like
it wants me to right click a file tree and make a new file using the tree, this
is not my jam.

Here is what I came up with to replace my til template.

```
---
date: <% tp.file.creation_date() %>
templateKey: til
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
  -
---
<%*
const fileName = originalFileName.toLowerCase().replace(/\s+/g, '-');
const newFilePath = `pages/til/${fileName}`;
await tp.file.move(newFilePath);
-%>

<% tp.file.cursor() %>
```

* `tR` is a return value, and it gets placed directly into the place it is in the file
* `to.file.cursor()` creates a tab-index point so I can tab into the content
