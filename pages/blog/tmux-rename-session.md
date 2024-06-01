---
Tags: ['cli', 'linux', 'tmux',]
templateKey: blog-post
title: tmux rename session
date: 2021-08-03T23:51:21
published: true

---

[https://youtu.be/WRLRiQDjVIA](https://youtu.be/WRLRiQDjVIA){.hoverlink}

So you have been working on your tmux workflow, you've dropped a too many
window workflow for scoping work that belongs together into separate sessions,
but you cannot remember what session your work is in. If your diligent you have
named your window when you created it, but sometimes its intent has changed or
your were just plain too lazy at the time for the extra characters needed to
name it.  Don't worry we can still give that session a descriptive name.

Let's rename some sessions in the terminal.

``` bash
# rename the current session to me
tmux rename-session me

# rename the me session to scratch
tmux rename-session -t me scratch
```

There is a default keybinding that you can use `<prefix>+$` to rename the
current session in the tmux command line.

``` bash
bind-key          $ command-prompt -I #S "rename-session '%%'"
```

I've also had this keybinding kicking around for years, but I rarely use it
anymore. You will see why in an upcoming video.

``` python
bind -n M-W command-prompt "rename-session '%%'"
```

[[ tmux-nav-2021 ]]

> for more information on how I navigate tmux, check out this full post

Also check out the full YouTube
[tmux-playlist](https://www.youtube.com/playlist?list=PLTRNG6WIHETB4reAxbWza3CZeP9KL6Bkr)
to see all of the videos in this series.
