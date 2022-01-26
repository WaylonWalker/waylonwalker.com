---
date: 2022-01-26 02:50:56.920579
templateKey: til
title: Tmux and Vim Clipboard for Ubuntu
tags:
  - linux
  - vim
  - tmux

---

One of the first things I noticed broken in my terminal based workflow moving
from Windows wsl to ubuntu was that my clipboard was all messed up and not
working with my terminal apps.  Luckily setting tmux and neovim to work with
the system clipboard was much easier than it was on windows.

First off you need to get `xclip` if you don't already have it provided by your
distro.  I found it in the apt repositories.  I have used it between Ubuntu
18.04 and 21.10 and they all work flawlessly for me.

I have tmux setup to automatically copy any selection I make to the clipboard
by setting the following in my `~/.tmux.conf`. While I have neovim open I need
to be in insert mode for this to pick up.

``` bash
# ~/tmux.conf
bind -T copy-mode-vi Enter send-keys -X copy-pipe-and-cancel "xclip -i -f -selection primary | xclip -i -selection clipboard"
bind-key -T copy-mode-vi MouseDragEnd1Pane send-keys -X copy-pipe-and-cancel "xclip -selection clipboard -i"
```

To get my yanks to go to the system clipboard in neovim, I just added
unnamedplus to my existing clipboard variable.

``` vim
# ~/.config/nvim/init.vim
set clipboard+=unnamedplus
```

If you need to copy something right from the terminal you can use xclip
directly.  I do this semi-often to send someone a message in chat.

``` bash
cat file.txt | clip -sel copy
```

I set up some alias's for doing this a bit more efficiently, but don't find
myself using them very often.  This helps me grab commands from history and
copy them.

``` bash
alias hclip="history | tail -n1 | cut -c 8- | xclip -sel clip"
alias fclip="history -n 1000 | fzf | cut -c 8- | xclip -sel clip"
alias fclip="history -n 1000 | fzf | xclip -sel clip"
```
