---
date: <% tp.date.now("YYYY-MM-DD HH:mm:ss") %>
templateKey: daily
title: <% tp.date.now("YYYY-MM-DD") %> Notes
published: true
<%*
  // Folder where daily notes live
  const targetDir = "daily/pages/daily";

  // File name for today
  const fileName = `${tp.date.now("YYYY-MM-DD")}-notes.md`;

  // Full relative path
  const newPath = `${targetDir}/${fileName}`;

  // Move current file to correct location/name
  await tp.file.move(newPath);
%>
---
