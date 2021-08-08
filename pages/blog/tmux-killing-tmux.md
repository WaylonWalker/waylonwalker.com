---
Tags: ['cli', 'linux', 'tmux',]
templateKey: blog-post
title: killing tmux
date: 2021-08-11T09:03:09
status: published

---

Now it's time to switch gears, we are onto a different part of our day and
there are just too many sessions running and we need to clean up shop.

## kill-server

One viable option is to nuke the whole dang thing.  I actually do this more
than you might think.

``` bash
tmux kill-server
```

> save and commit your work diligently before `kill-server`

## kill-session

A more reasonable option might be to kill a single session.

``` bash
# kills the current session
tmux kill-session

# kills the session named scratch
tmux kill-session scratch
```

## choose-tree

Killing sessions one by one from the command line can be a bit tedious, and
involve more keystrokes than necessary.  Another option built right into tmux
is `choose-tree`.  By default `choose-tree` is bound to `prefix+s`, that's
pressing control+b then s.  Once you are in `choose-tree`, you can navigate
around with your configured navigation scheme, press `x` to kill a session, or
pane or window then `y` to confirm.  You can also batch delete by tagging items
with t, and killing them all at once with `X`.

https://waylonwalker.com/tmux-choose-tree/

> check out this post for a bit more information on choose-tree

## fuzzy matcher

Here is my preferred way, using a fuzzy matcher.  I recently improved this one
by making it a popup and cleaning it up based on a repsonse,
[tmux-output-formatting](https://qmacro.org/autodidactics/2022/08/06/tmux-output-formatting/)
by [DJ Adams](https://twitter.com/qmacro).  I press prefix+k to bring up a kill-session menu.

``` bash
bind k display-popup -E "\
    tmux list-sessions -F '#{?session_attached,,#{session_name}}' |\
    fzf --reverse -m --header=kill-session |\
    xargs -I {} tmux kill-session -t {}"
```

> note this is setup to multiple sessions all at once.

https://waylonwalker.com/tmux-nav-2021/

> for more information on how I navigate tmux, check out this full post


Also check out the full YouTube
[tmux-playlist](https://www.youtube.com/playlist?list=PLTRNG6WIHETB4reAxbWza3CZeP9KL6B)
to see all of the videos in this series.

