---
title: '💭 Alir3z4/html2text: Convert HTML to Markdown-formatted text.'
date: 2024-05-01T17:50:26
templateKey: link
link: https://github.com/Alir3z4/html2text
tags:
  - 
published: true

---

> Super neat tool to convert html to markdown

``` python
>>> import html2text
>>>
>>> print(html2text.html2text("<p><strong>Zed's</strong> dead baby, <em>Zed's</em> dead.</p>"))
**Zed's** dead baby, _Zed's_ dead.
```

It even plays nicely with rich.

``` python
from rich.markdown import Markdown
from rich.console import Console
import html2text
console = Console()
md = Markdown(html2text.html2text("<p><strong>Zed's</strong> dead baby, <em>Zed's</em> dead.</p>"))
console.print(md)
``` 

[Original thought](https://github.com/Alir3z4/html2text)
