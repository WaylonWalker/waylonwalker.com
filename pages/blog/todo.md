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

I see you there, trying to script out your tmux layouts. Tryig to get each
project setup just perfect with a script, but you keep stumbling over yourself
with `duplicate session` error messages

The `has-session` tmux command is a handy tool to prevent this `duplicate
session` error message when scripting your tmux layouts.

## command line

The command is pretty straight forward, you simply ask tmux if the session name
you are looking for exists.

``` bash
tmux has-session -t "waylonwalker_com"
```

# killing tmux

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


# display-message

You've got some long running tasks, and you're trying to stay productive and
knock tasks off that board, but you keep finding that your processes finish and
you stay on other tasks for longer than you should.  You were in the flow and
just did not check back in on it.  With `display-message` you can send yourself
a notification when that long running task is complete.

## from the man page

Here is a snippet of `display-message` from the tmux man page.  I rarely need
to do anything other than just display message, but there are other flags for
it.

``` bash
display-message [-aINpv] [-c target-client] [-d delay] [-t target-pane] [message]
            (alias: display)

        Display a message.  If -p is given, the output is printed to stdout,
        otherwise it is displayed in the target-client status line for up to
        delay milliseconds.  If delay is not given, the message-time option is
        used; a delay of zero waits for a key press.  ‘N’ ignores key presses
        and closes only after the delay expires.  The format of message is
        described in the FORMATS section;

        information is taken from target-pane if -t is given, otherwise the
        active pane.

        -v prints verbose logging as the format is parsed and -a lists the
        format variables and their values.

        -I forwards any input read from stdin to the empty pane given by
        target-pane.
```

## notifier

With `display-message` we can do things like setup notifications that will work cross platform.

``` bash
cmatrix -t 2 && tmux display-message done
```

Without setting the target-pane `display-message` defaults to the active pane.
This is a very handy feature that allows us to switch windows, or sessions and
still recieve the message.

# ta

Now your creating, jumping, and killing sessions like a boss. You are slicing
through projects with ease, let me show you one more thing that can be the
cream on top of this silky smooth setup we have been working towards.

## [Chris Toomey's](https://twitter.com/christoomey) Tmux Course

This script is simply my fork of Chris Toomey's `tat` script straight out of
his course.  It helps us create or jump to project specific sessions with ease.

## a directory of projects

My version of the `ta` script will let you pass it a directory, and it will
give you a fuzzy popup.

``` bash
ta ~/git
```

## setting up a keybinding

``` bash
bind C-g display-popup -E "ta ~/git"
```

![ta-git](https://images.waylonwalker.com/ta-git.png)

## default layout

By default I have my projects open with a vertical split, vim is on top, with
my file finder open and the lower split is set to just my terminal.  This is
what I do 90% of the time that I open a project anyways.

![ta-git-layout](https://images.waylonwalker.com/ta-git-layout.png)

## More projects

I also have a directory setup that is a symlink-gallery of all of my projects,
both private and public.  This makes it easy to have one key that lets me see
all of my projects.

```bash
rm -rf ~/projects
mkdir ~/projects
ln -sf ~/work/* ~/projects
ln -sf ~/git/* ~/projects
```

https://waylonwalker.com/symlink-gallery/

> This post covers how I combine all my projects into a single directory.

## Related Links

* [default key bindings](https://gist.github.com/mzmonsour/8791835)
* [Chris Toomey's](https://twitter.com/christoomey) Tmux Course
* my [ta script](https://github.com/WaylonWalker/devtainer/blob/main/bin/.local/bin/ta)
* my [.tmux.conf](https://github.com/WaylonWalker/devtainer/blob/main/tmux/.tmux.conf)

# show-messages

As we push the limits of tmux further and further you are bound to end up in a
situation where you are mashing down a hotkey and it's just not doing what you
want it to do, and you have no idea why.

`show-messages` is a tmux command that can be used to show what tmux is
actually doing behind the scenes.  This might highlight any hot key conflicts
you might have in your `~/.tmux.conf`.

## man page for show-messages

In case you wnat more information about show-messages, here is the man page.

``` bash
show-messages [-JT] [-t target-client]
            (alias: showmsgs)

        Show server messages or information.  Messages are stored, up to a
        maximum of the limit set by the message-limit server option.  -J and -T
        show debugging information about jobs and terminals.
```


# using popups to send alerts
# putting it all together
