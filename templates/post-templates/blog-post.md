---
date: <% tp.file.creation_date() %>
templateKey: blog
title:
published: true
tags:
  -
---
<%*
const originalFileName = await tp.system.prompt("Enter file name");
const fileName = originalFileName.toLowerCase().replace(/\s+/g, '-');
const newFilePath = `pages/blog/${fileName}`;
await tp.file.move(newFilePath);
-%>
