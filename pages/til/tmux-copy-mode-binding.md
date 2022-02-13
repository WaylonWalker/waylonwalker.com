---
date: 2022-02-13 17:05:23.746243
templateKey: til
title: A better copy-mode bind for Tmux
tags:
  - tmux
  - cli

---

The default keybinding for copy-mode `<prefix>-[` is one that is just so
awkward for me to hit that I end up not using it at all.  I was on a
call with my buddy Nic this week and saw him just fluidly jump into
`copy-mode` in an effortless fashion, so I had to ask him for his
keybinding and it just made sense. Enter, that's it.  So I have addedt
his to my `~/.tmux.conf` along with one for `alt-enter` and have found
myself using it way more so far.

## Setting copy-mode to enter

To do this I just popped open my `~/.tmux.conf` and added the following.
Now I can get to `copy-mode` with `<prefix>-Enter` which is `control-b
Enter`, or `alt-enter`.

```bash
bind Enter copy-mode
bind -n M-Enter copy-mode
```

## More on copy-mode

I have a full video on copy-mode you can find here.

https://waylonwalker.com/tmux-copy-mode/
