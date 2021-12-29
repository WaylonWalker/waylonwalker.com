---
date: 2021-12-30T15:26:01
templateKey: til
title: My first impressions with pyenv
tags:
  - python
  - linux
  - bash

---


``` bash
pyenv install --list
pyenv install 3.8.12
pyenv local python3.8.12
pyenv exec pip install pipx
pyenv exec pipx run kedro new
pyenv exec python -m venv .venv --prompt $(basename $PWD)
```

## Links
https://github.com/pyenv/pyenv#installation
