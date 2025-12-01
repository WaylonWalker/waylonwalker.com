---
date: 2025-06-05 20:37:10
templateKey: til
title: rich theme
published: true
tags:
  - python

---

The rich console is themeable, I've been a long time user of rich and had no
Idea.  You can define your own theme keywords and use them just like you use
normal rich keywords in square brackets like`'[bold red]'`.

``` python
from rich.console import Console
from rich.theme import Theme
custom_theme = Theme({
    "info": "dim cyan",
    "warning": "magenta",
    "danger": "bold red"
})
console = Console(theme=custom_theme)
console.print("This is information", style="info")
console.print("[warning]The pod bay doors are locked[/warning]")
console.print("Something terrible happened!", style="danger")
```
