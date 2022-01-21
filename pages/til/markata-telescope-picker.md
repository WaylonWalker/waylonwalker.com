---
date: 2022-01-23 04:52:20.855900
templateKey: til
title: Markata Filters as Telescope Pickers in Neovim
tags:
  - python
  - cli
  - vim

---

``` python
nnoremap geit <cmd>Telescope find_files find_command=markata,list,--map,path,--filter,date==today<cr>
nnoremap geil <cmd>Telescope find_files find_command=markata,list,--map,path,--filter,templateKey=='til',--sort,date,--reverse<cr>
nnoremap geig <cmd>Telescope find_files find_command=markata,list,--map,path,--filter,templateKey=='gratitude',--sort,date,--reverse<cr>
```
