---
templateKey: blog-post
title: Keyboard Driven VSCode
date: 2019-07-07T05:00:00.000+00:00
published: true
description: Reimagining my tmux configuration inside of vscode.
tags:
  - vscode
  - tmux
---
> Throw that mouse Away its time to setup some keyboard shortcuts.

These sortcuts were the baseline for switching from tmux/vim to vscode.  Most folks posts I was able to find gave great tips on replacing vim, but very few have focused on the hackability of tmux.  tmux allows me to rapidly fire up a workspace, create new windows and splits.  Then When I switch tasks I can leave that workspace open and and jump right back in later exactly where I left off.  There is nothing quite like it.  The shortcuts listed here make the transition a bit better. The worst thing I found when using vscode at first was no way to switch between the terminal and editor without the mouse.  This first set of keybindings solve that issue.

> The worst thing I found when using vscode at first was no way to switch between the terminal and editor without the mouse.

!!! see-also
 I have an updated article in my tmux workflow [[tmux-nav-2021]]

## Alt+\[hjkl\]

_navigation_

⬅ jump to **left** split **alt+h**

⬇ jump to **terminal** from editor **alt+j**

⬆ jump to **editor** from terminal **alt+k**

➡ jump to **right** split **alt+l**

This is by var the most useful set of keybindings that I use in vscode and is directly replicated from my tmux configuration.  It allows me to quickly jump up, down, left, right.  Do note that if you use vertical splits it does not work as well as tmux 😢.

![navigating vscode with keyboard shortcuts](https://dropper.waylonwalker.com/file/14099538-c447-4c61-a2cd-c0e6b1a8f734.mp4)

``` json
[
        {
            "key": "alt+j",
            "command": "workbench.action.terminal.focus",
            "when": "editorFocus"
        },

        {
            "key": "alt+k",
            "command": "workbench.action.focusFirstEditorGroup",
            "when": "terminalFocus"
        },
        {
            "key": "alt+k",
            "command": "workbench.action.focusAboveGroup",
            "when": "editorFocus"
        },
        {
            "key": "alt+l",
            "command": "-toggleFindInSelection",
            "when": "editorFocus"
        },
        {
            "key": "alt+l",
            "command": "workbench.action.focusNextGroup",
            "when": "editorFocus"
        },
        {
            "key": "alt+h",
            "command": "workbench.action.focusPreviousGroup",
            "when": "editorFocus"
        },

        {
            "key": "alt+l",
            "command": "workbench.action.terminal.focusNextPane",
            "when": "terminalFocus"
        },
        {
            "key": "alt+h",
            "command": "workbench.action.terminal.focusPreviousPane",
            "when": "terminalFocus"
        },
]
```

## Alt+b

_toggle bloat_

Since closing the sidebar is assigned to `ctrl+b` I thought that it made most sense to simulate the activity bar with `alt+b`.  There are many times when I just want to get as much out of the way as possible and this little bit does help.

![hiding the activity bar ](https://dropper.waylonwalker.com/file/9d242951-baed-4d2d-813d-753e56290972.mp4)

``` json
[
    {
        "key": "alt+b",
        "command": "workbench.action.toggleActivityBarVisibility",
        "when": "editorFocus"
    },
]
```

## Alt+\[svx\]

_Split it up_

🙌 Split hoizontally **alt+s**

🍌 Vertically **alt+v**

💥 Close **alt+x**

This is another one replicated from tmux for quickly creatiting horizontal (s) and vertical (v) splits.  Once I am done with them I can close them with alt+x.

![Make and destroy splits with ease in vscode.](https://dropper.waylonwalker.com/file/b073a7cf-01ff-4705-ae11-e6cd41109792.mp4)

``` json
[
    {
        "key": "alt+s",
        "command": "workbench.action.terminal.split",
        "when": "terminalFocus"
    },
    {
        "key": "alt+s",
        "command": "workbench.action.splitEditor",
        "when": "editorFocus"
    },
    {
        "key": "alt+v",
        "command": "workbench.action.splitEditorOrthogonal",
        "when": "editorFocus"
    },
    {
        "key": "alt+x",
        "command": "workbench.action.terminal.kill",
        "when": "terminalFocus"
    },
    {
        "key": "alt+x",
        "command": "workbench.action.closeActiveEditor",
        "when": "editorFocus"
    }
]
```

## Alt+\[cnp\]

🤲 **Create** new workspace **alt+c**

⏭ jump to **next** workspace **alt+n**

⏮ jump to **previous** workspace **alt+p**

Sometimes the terminal window gets a bit cramped inside of splits and you need to use different panes.  I replicated the cnp pattern from tmux here as well.  I can create (c) new panes, then go to the next (n), or previous (p) without leaving the comfort of my keyboard.

I am often using this one when I have a process running that I watch like gatsby, and I need to quickly pop into a new pane to run a git command and back in to gatsby before jumping up to my editor.

![](https://dropper.waylonwalker.com/file/f8c775ad-514a-4b7d-a823-27885da8a2df.mp4)

``` json
[
    {
        "key": "alt+c",
        "command": "workbench.action.terminal.new",
        "when": "terminalFocus"
    },
    {
        "key": "alt+n",
        "command": "workbench.action.terminal.focusNext",
        "when": "terminalFocus"
    },

    {
        "key": "alt+p",
        "command": "workbench.action.terminal.focusPrevious",
        "when": "terminalFocus"
    },
]
```

## Alt+z

🗻 Zoom into terminal **alt+z**

This last one doesnt work as well as I would like but it sure does get the job done.  It Zooms (z) into the terminal from anywhere in vscode.  I can be in my editor and zoom out of the terminal to make more room, or zoom in to see what happened from my last edit.

![](https://dropper.waylonwalker.com/file/a70d8ace-1cf3-4d71-aa72-c27ef1f07cf9.mp4)

``` json
[
    {
        "key": "alt+z",
        "command": "workbench.action.toggleMaximizedPanel",
    },
]
```

## Bonus

## Alt+r

🖱 right click in place

I recently found this one, and find it quite useful to quickly do things like revert selected range, or extract variable without leaving the keyboard.

``` json
[
  {
    "key": "alt+r",
    "command": "editor.action.showContextMenu",
  },
]
```
