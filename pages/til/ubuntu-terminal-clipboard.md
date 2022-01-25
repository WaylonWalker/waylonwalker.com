---
date: 2022-01-25 02:50:56.920579
templateKey: til
title: Tmux and Vim Clipboard for Ubuntu
tags:
  - linux
  - vim
  - tmux

---


~/tmux.conf
```
bind -T copy-mode-vi Enter send-keys -X copy-pipe-and-cancel "xclip -i -f -selection primary | xclip -i -selection clipboard"
```

```
set clipboard+=unnamedplus
```

```
cat file.txt | clip -sel copy
```
