---
date: 2025-11-26 13:24:38
templateKey: til
title: COLUMNS env var
published: true
tags:
  - python
  - bash
  - terminal

---

setting `COLUMNS` env var to a number greater than 0 will make the terminal resize to that number of columns.

``` bash
COLUMNS=80 uvx --from rich-cli rich myscript.py
```

!!! NOTE

    Not all programs respct the `COLUMNS` env var, but rich does, and a lot of
    stuff I'm building uses rich.

I discovered this when I was trying to make a low effort readme generated from
the code, but did not depend on the size of terminal it was ran on.

``` bash
# justfile
readme:
    echo "# Workspaces" > README.md
    echo "" >> README.md
    echo '``` bash' >> README.md
    COLUMNS=80 ./workspaces.py --help >> README.md
    echo '```' >> README.md
```
