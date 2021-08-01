---
Tags: ['cli', 'linux', 'tmux',]
templateKey: blog-post
title: tmux start application
date: 2021-08-03T23:51:21
status: published

---

Scripting tmux to open up specific applications can be intimidating your first
time.  It can be tricky to get it to start in the right directory.  If you are
trying to assign applictaions to a keybinding it can be easy to mess up and
have weird things happen every time your `~/.tmux.conf` gets sourced.

## Open htop in an above split

I used this one for a number of years to take a quick peek into my systems
performance while a memory intensive task was running.

``` bash
bind -n M-t split-window htop \; swap-pane -U
```

> 🗒️ note that the `swap-pane -U` will make the htop split active immediately

## Open htop in a popup

With the new tmux popup windows I really like the flow of just peeking at
htop in a popup and jumping back into what I was doing.  It can have a more
consistennt look, and not mess with the window layouts.

``` bash
bind -n M-t popup -E -h 95% -w 95% -x 100% "htop"
```

## Open an applicaiton in the current directory

One thing that can be tricky is getting apps that need to be in a specific
directory started in the directory that you want. Here are two examples I use
to open `vifm` or `gitui`. 

``` bash
bind -n M-e split-window -c '#{pane_current_path}' vifm . .\; resize-pane -Z;
bind C-k split-window -c '#{pane_current_path}' 'gitui'\; resize-pane -Z;
```

> 🗒️ note that `split-window` takes in a -c flag before the application you
> want to run to specify the startup directory.

## Open a popup in a specific directory

I've been converted over to using popups for these as well.  I'll admit that
the workflow of creating a new full screen window may have been better, but
this can be a bit less jarring, espessially if you have anyone following
along with what you are doing.

``` bash
bind -n M-e display-popup -d '#{pane_current_path}' -E vifm
bind C-k display-popup -d '#{pane_current_path}' -E 'gitui'
```

https://waylonwalker.com/tmux-nav-2021/

> for more information on how I navigate tmux, check out this full post


Also check out the full YouTube
[tmux-playlist](https://www.youtube.com/playlist?list=PLTRNG6WIHETB4reAxbWza3CZeP9KL6B)
to see all of the videos in this series.



