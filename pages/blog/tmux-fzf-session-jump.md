---
Tags: ['cli', 'linux', 'tmux',]
templateKey: blog-post
title: tmux fzf session jumper
date: 2021-08-05T09:03:09
published: true

---

https://youtu.be/DkJ9rb85LC0

Quickly getting between tmux splits is critical skill for productivity.  You
can get by with `next` or `prev` session for awhile, but if you have more than
about three session you need something a bit more targeted.


## Full Screen selector

I have used this fzf one keybinding for quite awhile,  honestly I did not make
it up, and cannot remember where it came from. It will open up a session picker
in a new full screen window.

``` bash
bind C-j new-window -n "session-switcher" "\
    tmux list-sessions -F '#{?session_attached,,#{session_name}}' |\
    sed '/^$/d' |\
    fzf --reverse --header jump-to-session --preview 'tmux capture-pane -pt {}'  |\
    xargs tmux switch-client -t"

```

## Popup selector

Like with many of my keybindings I have swapped this one out for a popup
version.  It just feels so smooth.

``` bash
bind C-j display-popup -E "\
    tmux list-sessions -F '#{?session_attached,,#{session_name}}' |\
    sed '/^$/d' |\
    fzf --reverse --header jump-to-session --preview 'tmux capture-pane -pt {}'  |\
    xargs tmux switch-client -t"
```

https://waylonwalker.com/tmux-nav-2021/

> for more information on how I navigate tmux, check out this full post


Also check out the full YouTube
[tmux-playlist](https://www.youtube.com/playlist?list=PLTRNG6WIHETB4reAxbWza3CZeP9KL6Bkr)
to see all of the videos in this series.
