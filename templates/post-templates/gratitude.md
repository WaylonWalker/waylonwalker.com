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
const postCount = files.filter(file => file.startsWith("gratitude-")).length + 89;
const newFilePath = `/pages/gratitude/gratitude-${postCount}.md`;
await tp.file.move(newFilePath);
%>

---
