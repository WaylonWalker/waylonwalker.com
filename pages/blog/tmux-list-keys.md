---
Tags: ['cli', 'linux', 'tmux',]
templateKey: blog-post
title: tmux list-keys
date: 2021-08-08T09:03:09
status: published

---

https://youtu.be/Y1MYmL8ZolE

Tmux list keys can be a useful tool to help remind you of what kebindings you
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

        List key bindings.  There are two forms: the default lists keys as
        bind-key commands; -N lists only keys with attached notes and shows
        only the ke y and note for each key.

        With the default form, all key tables are listed by default.  -T lists only keys in key-table.

        With the -N form, only keys in the root and prefix key tables are
        listed by default; -T also lists only keys in key-table.  -P specifies
        a prefix to print before each key and -1 lists only the first matching
        key.  -a lists the command for keys that do not have a note rather than
        skipping them.

```

https://waylonwalker.com/tmux-nav-2021/

> for more information on how I navigate tmux, check out this full post


Also check out the full YouTube
[tmux-playlist](https://www.youtube.com/playlist?list=PLTRNG6WIHETB4reAxbWza3CZeP9KL6Bkr)
to see all of the videos in this series.
