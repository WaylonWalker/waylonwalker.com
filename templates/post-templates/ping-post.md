---
date: <% tp.file.creation_date() %>
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
  -
---
