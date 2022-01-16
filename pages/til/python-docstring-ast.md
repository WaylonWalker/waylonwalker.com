---
date: 2022-01-18 20:13:32.860641
templateKey: til
title: Get Python docstring with ast
tags:
  - python

---

```python
raw_tree = py_file.read_text()
tree = ast.parse(raw_tree)

```
