---
date: 2022-01-12 03:25:36.794864
templateKey: til
title:
tags:
  - linux
  - blog
  - cli

---


``` python
sudo apt install \
  pandoc \
  texlive-latex-base \
  texlive-fonts-recommended \
  texlive-extra-utils \
  texlive-latex-extra \
  texlive-xetex
```

``` python
pandoc bash.md -o bash.pdf --latex-engine=xelatex
```
