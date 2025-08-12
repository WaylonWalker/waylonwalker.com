---
date: <% tp.file.creation_date() %>
templateKey: gratitude
published: true
tags:
- gratitude
<%*
const fs = require('fs');
const folderPath = app.vault.adapter.basePath + "/pages/gratitude";
const files = fs.readdirSync(folderPath);
const postCount = files.filter(file => file.startsWith("gratitude-")).length + 2;
const newFilePath = `/pages/gratitude/gratitude-${postCount}`;
await tp.file.move(newFilePath);
%>

---
