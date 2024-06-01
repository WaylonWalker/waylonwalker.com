---
templateKey: blog-post
tags: ["cli", "linux", "tmux"]
title: tmux choose-tree
date: 2021-07-19T23:51:21
published: true
---

[https://youtu.be/79Y-kqAiMpw](https://youtu.be/79Y-kqAiMpw){.hoverlink}

Choose tree is a powerful tmux utility that provides a graphical interface to
preview all sessions, windows, and panes, move between them kill them, move
them and much more.

The default keybinding

```bash
bind-key -T prefix s choose-tree -s
```

my preferred keybinding to open sessions and windows collapsed and Zoomed in.

```bash
bind-key j choose-tree -swZ
```

From the man page.

```bash
choose-tree [-GNrswZ] [-F format] [-f filter] [-K key-format] [-O sort-order] [-t target-pane] [template]
        Put a pane into tree mode, where a session, window or pane may be chosen interactively from a tree.  Each session, window or pane is shown on
        one line.  A shortcut key is shown on the left in brackets allowing for immediate choice, or the tree may be navigated and an item chosen or
        otherwise manipulated using the keys below.  -s starts with sessions collapsed and -w with windows collapsed.  -Z zooms the pane.  The follow‐
        ing keys may be used in tree mode:

            Key    Function
            Enter  Choose selected item
            Up     Select previous item
            Down   Select next item
            +      Expand selected item
            -      Collapse selected item
            M-+    Expand all items
            M--    Collapse all items
            x      Kill selected item
            X      Kill tagged items
            <      Scroll list of previews left
            >      Scroll list of previews right
            C-s    Search by name
            m      Set the marked pane
            M      Clear the marked pane
            n      Repeat last search
            t      Toggle if item is tagged
            T      Tag no items
            C-t    Tag all items
            :      Run a command for each tagged item
            f      Enter a format to filter items
            H      Jump to the starting pane
            O      Change sort field
            r      Reverse sort order
            v      Toggle preview
            q      Exit mode

        After a session, window or pane is chosen, ‘%%’ is replaced by the target in template and the result executed as a command.  If template is
        not given, "switch-client -t '%%'" is used.

        -O specifies the initial sort field: one of ‘index’, ‘name’, or ‘time’.  -r reverses the sort order.  -f specifies an initial filter: the fil‐
        ter is a format - if it evaluates to zero, the item in the list is not shown, otherwise it is shown.  If a filter would lead to an empty list,
        it is ignored.  -F specifies the format for each item in the tree and -K a format for each shortcut key; both are evaluated once for each
        line.  -N starts without the preview.  -G includes all sessions in any session groups in the tree rather than only the first.  This command
        works only if at least one client is attached.
```

[https://waylonwalker.com/tmux-nav-2021/](https://waylonwalker.com/tmux-nav-2021/){.hoverlink}

> for more information on how I navigate tmux, check out this full post
