---
templateKey: blog-post
tags: ['linux']
title: I am moving from windows to Ubuntu here are some of my notes
date: 2021-06-25T20:50:45
status: draft

---

## gnome-tweaks

``` bash
sudo apt install gnome-tweaks

```

## nordix gtk theme

I ran this, but have no idea if it had any effect as the theme did
not show up until I relogged.

```
gsettings set org.gnome.desktop.wm.preferences theme Nordic
```

What I think actuagnome terminal showing scrollbar in tmuxlly worked was 

## Get that dock outta here

I tried to disable the dock and it didn't immediately work for me,
likely because I needed to relog.  I really have no use for the
dock though as I will always open applications with a hotkey or
super + search.

``` bash
sudo apt remove gnome-shell-extension-ubuntu-dock
```

## Terminal One Dark Theme

I don't stress too hard on themes, I just want something halfway consistent and
just works.  I typically have just used a semi-popular theme "one-dark"
everywhere.  This was the default theme in GitHub's Atom text editor that I
never used.  I only care that it looks good and is popular enought that it just
exists everywhere.

``` bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/denysdovhan/gnome-terminal-one/master/one-dark.sh)"
```

## Terminal menu and scrollbar

I found these to be ugly ans unnecessary so I turned them off.  You can access
all the menu items by right clicking on the terminal anyways, so there is no
reason to let it take up any screen real estate.

### Hiding the scrollbar

![hide the scrollbar](https://images.waylonwalker.com/gnome-terminal-hide-scrollbar)

### Hiding the menubar

![hide the menubar](https://images.waylonwalker.com/gnome-terminal-hide-menubar)

## vim clipboard

``` bash
sudo apt install xsel
```

``` vim
set clipboard+=unnamedplus
```

## tmux clipboard

``` bash
# Copy and Paste on Linux
bind -T copy-mode-vi Enter send-keys -X copy-pipe-and-cancel "xclip -i -f -selection primary | xclip -i -selection clipboard"
set-option -s set-clipboard off
bind-key -T copy-mode-vi MouseDragEnd1Pane send-keys -X copy-pipe-and-cancel "xclip -selection clipboard -i"
```

## Hotkeys

### screenshots

I am constantly taking screenshots for my daily workflow, on Windows I had it
setup to both send to the clipboard and store in a screenshots directory.

``` bash
# take a screenshot and Store it as a file.
gnome-screenshot -a

# take a screenshot and send it to the clipboard
gnome-screenshot -ac
```

