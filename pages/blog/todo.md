---
templateKey: blog-post
tags: []
title: Todo
date: 2021-01-01T00:00:00
status: draft

---

This week in tmux

* source-file
* tat
* status bar
* list-keys
* has-session
* killing tmux
* display-message
* show-messages
* using popups to send alerts
* putting it all together

## kedro YouTube series

Get started on daily kedro shorts, these are indended to be short clips that
people can watch a playlist and learn about kedro concepts at their own pace.
This is meant to be low barrier to entry for me to create.  Like the tmux
series, I hope to make a sub three minute video within one or two takes, no
edits, all straight from obs.

* whatis kedro
* kedro new
* kedro install
* kedro pipeline create
* making your first nodes in kedro
* kedro run
* kedro catalog create
* listing things from the kedro cli
    * kedro catalog list
    * kedro pipeline list
* modular piplines
    * kedro pipeline package
    * kedro pipeline pull
* Storing catalog entries
* parameters
* pipeline registry
* find-kedro
* lambdas in kedro nodes
* built in pipeline filters from the
* filtering pipelines with list comps
* globbing for catalog entries in the repl
* activate-nbstripout
* build-docs         
* build-reqs         
* kedro package
* kedro lint
* kedro test
* kedro ipython
* kedro jupyter
* kedro spaceflights the gold standard of tutorials
* speed up your kedro pipeline with a sane `__default__`
* create custom kedro cli commands
* override kedro cli commands
* accessing the kedro session
* installing kedro hooks 
* creating your first kedro hook

## wip posts

# tmux-source-file

So you have been tricking out that `.tmux.conf`, you're looking for a silky
smooth workflow that lets you fly through tmux with super speed, but every time
you tweak out that `.tmux.conf` you have to restart your whole session. Not amymore, 


Let's add this to the bottom of our tmux.conf so that you can see everytime it
gets sourced.

``` bash
display-message "hello beautiful"
```

## command

We can run this command from your shell to re-source your changed `.tmux.conf`

``` bash
tmux source-file ~/.tmux.conf
```

It also works from the tmux command line.

``` bash
source-file ~/.tmux.conf
```


## tmux hotkey

It's very common to set this up as a keybinding so that you can do it easily
without needing to memorize the exact command.

``` bash
bind -T prefix r source-file ~/.tmux.conf
bind -n M-r source-file ~/.tmux.conf
```

## from vim

This is my preferred way of re-sourcing my `.tmux.conf`.  It sits quietly in
the background, and I dont need to remember to do anything.  If you are a vim
user you can automate this process by creating a `autocmd bufwritepost`.  This
will shell out the `tmux source-file` everytime you save your `.tmux.conf`.

``` vim
autocmd bufwritepost .tmux.conf execute ':!tmux source-file %'
autocmd bufwritepost .tmux.local.conf execute ':!tmux source-file %'
```

# tat

# status bar

##  show the status bar

The tmux status bar can be a handy tool to remind yourself where you are within
tmux.  It can also include a bunch of system information like battery status,
cpu, mem, whatever you can get from the command  line.  Honestly I like to keep
it minimal, and actually keep it turned off most of the time.  I find that it
helps a little bit for others to follow along if I keep it on in certain
circumstances.

``` bash
bind s set-option -g status
bind C-s set-option -g status
```

## setting the background transparent

I really want a minimal status bar with very little bling, I want it to get out
of the way an not draw too much attention, so step one is to set the background to transparent.

``` bash
# default statusbar colors
#――――――――――――――――――――――――――――――――
set-option -g status-bg default
set-option -g status-fg colour240
```

## setting default colors

I want my status bar to somewhat match the rest of my theme, so I set the
default foreground as magenta and the default background as transparent.

``` bash
# default window title colors
#―――――――――――――――――――――――――――――――
set-window-option -g window-status-style fg=magenta
set-window-option -g window-status-style bg=default
```

## my status bar

Honestly I set this up quite awhile ago, and it does everything I need it to
for now.  It shows me the current session that I am in on the left and lists
out the windows for the session in the middle.

``` bash
set -g status-left-length 85
set -g status-left "working on#[fg=colour135] #S"
set -g window-status-current-format "#[fg=black,bold bg=default]│#[fg=white bg=cyan]#W#[fg=black,bold bg=default]│"
set -g window-status-current-format "#[fg=black,bold bg=default]│#[fg=colour135 bg=black]#W#[fg=black,bold bg=default]│"
set -g status-style bg=default
set -g status-right "#[fg=magenta] #[bg=gray] %b %d %Y %l:%M %p"
set -g status-right '#(gitmux "#{pane_current_path}")' 
set -g status-justify centre
```

# list-keys

Tmux list keys can be a useful tool to help remind you of what kebindinfs you
have setup.  You can search for them and scroll just like in tmux copy-mode.

## command line

You can call list-keys from the command line but the interface is not very
usable by itself.  It might be nice to mix with grep or a pager in some
circumstances.

``` bash
tmux list-keys
```

## tmux command line

Running `list-keys` from within the tmux command line puts you into a much more
pleasant `copy-mode`.

```
list-keys
```

## default keybinging

By default tmux comes with `list-keys` bound to prefix+?.

``` bash
bind-key          ? list-keys
```

## list-keys man page

You can see the additional flags provided by tmux in the man page for
`list-keys`.

``` bash
     list-keys [-1aN] [-P prefix-string -T key-table] [key]
                   (alias: lsk)
             List key bindings.  There are two forms: the default lists keys as bind-key commands; -N lists only keys with attached notes and shows only the ke
y and note for each key.

             With the default form, all key tables are listed by default.  -T lists only keys in key-table.

             With the -N form, only keys in the root and prefix key tables are listed by default; -T also lists only keys in key-table.  -P specifies a prefix
to print before each key and -1 lists only the
             first matching key.  -a lists the command for keys that do not have a note rather than skipping them.

```

# has-session
# killing tmux
# display-message
# show-messages
# using popups to send alerts
# putting it all together
