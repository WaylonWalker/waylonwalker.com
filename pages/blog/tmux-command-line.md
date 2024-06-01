---
templateKey: blog-post
tags: ['cli', 'linux', 'tmux',]
title: tmux command line
date: 2021-07-29T23:51:21
published: true

---

[https://youtu.be/SNu-4IrkjAs](https://youtu.be/SNu-4IrkjAs){.hoverlink}

So far we have covered a lot of tmux commands and how they map to keybindings
but these same commands can be executed at the command line.

## From the command line

Let's make a popup that displays our git status for 5s or until we close it
manually.  We can run the following command at the command line, in a split.

``` bash
tmux display-popup -E -d '#{pane_current_path}' 'git status && sleep 5'
```

## From the tmux command line

Or we can open the tmux command line and run it from tmux's built in command
line, which is very similar to bim EX mode. By default the tmux command line
can be opened with `prefix+[`.

``` bash
display-popup -E -d '#{pane_current_path}' 'git status && sleep 5'
```

> 🗒️ note that the tmux command is called by default when inside of tmux.

## Make it a keybinding

Finally we can make it a keybinding by adding a bind command ahead of our tmux
command, then we can execute this in the tmux command line or add it to our
`~/.tmux.conf`.

``` bash
bind s display-popup -E -d '#{pane_current_path}' 'git status && sleep 5'
```

[[ tmux-nav-2021 ]]

> for more information on how I navigate tmux, check out this full post

Also check out the full YouTube
[tmux-playlist](https://www.youtube.com/playlist?list=PLTRNG6WIHETB4reAxbWza3CZeP9KL6Bkr)
to see all of the videos in this series.
