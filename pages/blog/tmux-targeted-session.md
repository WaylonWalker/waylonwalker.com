---
tags: ['cli', 'linux', 'tmux',]
templateKey: blog-post
title: tmux targeted session
date: 2021-08-02T23:51:21
published: true

---

[https://youtu.be/5KE7Il7SOEk](https://youtu.be/5KE7Il7SOEk){.youtube-embed}

This is something that I made up but use every single day, this is what keeps
much of what is on my blog or my teams private work wiki going.  I have a few
very important directories that I have assigned directly to a hotkey for fast
session switching.

``` bash
bind -n M-i new-session -A -s waylonwalker_com "cd ~/git/waylonwalker.com/ && nvim"
bind i popup -E -h 95% -w 95% -x 100% "tmux new-session -A -s waylonwalker_com 'cd ~/git/waylonwalker.com/ && nvim'"
bind -n M-I popup -E "tmux new-session -A -s waylonwalker_com 'cd ~/git/waylonwalker.com/ && nvim'"
```

[[ tmux-new-session ]]

> This one is building off of yeserday's new-session post, make sure you check that one out as well.

[[ tmux-nav-2021 ]]

> for more information on how I navigate tmux, check out this full post

Also check out the full YouTube
[tmux-playlist](https://www.youtube.com/playlist?list=PLTRNG6WIHETB4reAxbWza3CZeP9KL6Bkr)
to see all of the videos in this series.
