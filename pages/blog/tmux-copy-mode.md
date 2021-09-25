---
templateKey: blog-post
tags: ['cli', 'linux', 'tmux',]
title: tmux copy-mode
date: 2021-07-28T23:51:21
status: published

---

https://youtu.be/-ypY_-VmBKk

tmux copy-mode is a tmux mode that lets you scroll, search, copy, and jump your
way through a pane.  There are a ton of keybindings for copy-mode, the main
ones you will need to know are `/` for searching down `?` for searching up, `n`
for next item, `space` for starting a selection, and enter to copy the
selection.  Arrow keys will be used for navigation unless you have specified vi mode, then it will be `hjkl`.

Default keybinding to get into copy mode is `prefix+[`.

``` bash
bind-key          [ copy-mode
```

If you are a vim user you will likely want to use vi style keys, add this to
your `~/.tmux.conf` file to enable vi mode.


``` bash
setw -g mode-keys vi
```

full list of copy-mode keybindings from the man page.

``` bash
  Command                                      vi              emacs
           append-selection
           append-selection-and-cancel                  A
           back-to-indentation                          ^               M-m
           begin-selection                              Space           C-Space
           bottom-line                                  L
           cancel                                       q               Escape
           clear-selection                              Escape          C-g
           copy-end-of-line [<prefix>]                  D               C-k
           copy-line [<prefix>]
           copy-pipe [<command>] [<prefix>]
           copy-pipe-no-clear [<command>] [<prefix>]
           copy-pipe-and-cancel [<command>] [<prefix>]
           copy-selection [<prefix>]
           copy-selection-no-clear [<prefix>]
           copy-selection-and-cancel [<prefix>]         Enter           M-w
           cursor-down                                  j               Down
           cursor-down-and-cancel
           cursor-left                                  h               Left
           cursor-right                                 l               Right
           cursor-up                                    k               Up
           end-of-line                                  $               C-e
           goto-line <line>                             :               g
           halfpage-down                                C-d             M-Down
           halfpage-down-and-cancel
           halfpage-up                                  C-u             M-Up
           history-bottom                               G               M->
           history-top                                  g               M-<
           jump-again                                   ;               ;
           jump-backward <to>                           F               F
           jump-forward <to>                            f               f
           jump-reverse                                 ,               ,
           jump-to-backward <to>                        T
           jump-to-forward <to>                         t
           jump-to-mark                                 M-x             M-x
           middle-line                                  M               M-r
           next-matching-bracket                        %               M-C-f
           next-paragraph                               }               M-}
           next-space                                   W
           next-space-end                               E
           next-word                                    w
           next-word-end                                e               M-f
           other-end                                    o
           page-down                                    C-f             PageDown
           page-down-and-cancel
           page-up                                      C-b             PageUp
           pipe [<command>] [<prefix>]
           pipe-no-clear [<command>] [<prefix>]
           pipe-and-cancel [<command>] [<prefix>]
           previous-matching-bracket                                    M-C-b
           previous-paragraph                           {               M-{
           previous-space                               B
           previous-word                                b               M-b
           rectangle-on
           rectangle-off
           rectangle-toggle                             v               R
           refresh-from-pane                            r               r
           scroll-down                                  C-e             C-Down
           scroll-down-and-cancel
           scroll-up                                    C-y             C-Up
           search-again                                 n               n
           search-backward <for>                        ?
           search-backward-incremental <for>                            C-r
           search-backward-text <for>
           search-forward <for>                         /
           search-forward-incremental <for>                             C-s
           search-forward-text <for>
           search-reverse                               N               N
           select-line                                  V
           select-word
           set-mark                                     X               X
           start-of-line                                0               C-a
           stop-selection
           top-line                                     H               M-R
```

https://waylonwalker.com/tmux-nav-2021/

> for more information on how I navigate tmux, check out this full post


Also check out the full YouTube
[tmux-playlist](https://www.youtube.com/playlist?list=PLTRNG6WIHETB4reAxbWza3CZeP9KL6B)
to see all of the videos in this series.

