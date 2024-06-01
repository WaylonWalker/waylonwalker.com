---
Tags: ['cli', 'linux', 'tmux',]
templateKey: blog-post
title: tmux new-session
date: 2021-08-01T23:51:21
published: true

---

[https://youtu.be/LbQNdCAUogE](https://youtu.be/LbQNdCAUogE){.hoverlink}

This one starts a new chapter in our series that is going to open up a whole
new set of workflow productivity options, understanding how the `new-session`
command is a critical command in our adventure into tmux glory.  This is going
to open the door for some seriously game changing hotkeys and scripting.

``` bash
# create a new session
tmux new-session

# create a new session detached
tmux new-session -d


# create a new session and name it
tmux new-session -s me

# create a new named session and attach to it if one exists
tmux new-session -As me
```

[[ tmux-nav-2021 ]]

> for more information on how I navigate tmux, check out this full post

Also check out the full YouTube
[tmux-playlist](https://www.youtube.com/playlist?list=PLTRNG6WIHETB4reAxbWza3CZeP9KL6Bkr)
to see all of the videos in this series.
