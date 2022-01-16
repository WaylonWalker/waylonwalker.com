---
date: 2022-01-17 15:16:33.238144
templateKey: til
title: Python Respect the .gitignore
tags:
  - python

---


```python

import pathspec
from pathlib import Path

markdown_files = Path().glob('**/*.md')
if (Path(".gitignore").exists():
    lines = Path(".gitignore").read_text().splitlines()

    spec = pathspec.PathSpec.from_lines("gitwildmatch", lines)

    markdown_files = [
        file for file in markdown_files if not spec.match_file(str(file))
    ]
```
