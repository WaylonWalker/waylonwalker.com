---
templateKey: blog-post
tags: ['linux']
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


## emoji support

One thing that I really missed quite early from windows was the emoji virtual
keyboard.  I like being able to quickly toss in those emoji that give just a
bit of a visual cue 🔥, ⚠️,, 🎉, 🦄, 💜. 


### installation

I found an application called emote. that seems to do everything I need it to
in the snap store.  Installation is a typicall snap install.

```
sudo snap install emote
```


### default keybinding


The application came with a default keybinding `ctrl+alt+e`, but I could never remember it.

```
ctrl+alt+e
```

### Windows keybinding

Old habits are hard to break, I opened up the gnome settings and set a hotkey
to `super+;` to run the command emote.

```
Super+;
```

### How it works



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

| Key | Desc | 
| --- | ---- |
| super+j | move to workspace below |
| super+k | move to workspace above |
| super+shift+j | move window one workspace down |
| super+shift+k | move window one workspace up |


| Key | Command | Desc | 
| --- | ------- | ---- |
| Super+e | nautilus | File Browser|
| Super+Shift+p | Area Screenshot | gnome-screenshot -a |
| Super+Alt+p | Area Screenshot to clipboard | gnome-screenshot -ac |
| Super+e | nautilus | File Browser|

### screenshots

I am constantly taking screenshots for my daily workflow, on Windows I had it
setup to both send to the clipboard and store in a screenshots directory.

``` bash
# take a screenshot and Store it as a file.
gnome-screenshot -a

# take a screenshot and send it to the clipboard
gnome-screenshot -ac
```

### obs

As od Jun 2021 the version of obs-studio installed using the instructions in
their wiki is out of date.  I had success getting the latest version, which
supports virtual webcams, using snap.

``` bash
sudo snap install obs-studio
```

### virtual webcam

After getting the latest version of obs-studio whixh supports virtual webcam it
still did not start.  After some searching I found that updating v4l2loopback
resolved the issue.

``` bash
sudo apt purge v4l2loopback-dkms
git clone https://github.com/umlaeute/v4l2loopback.git ~/git/v4l2loopback/
cd ~/git/v4l2loopback/
make
sudo make install
sudo modprobe v4l2loopback devices=1 exclusive_caps=1
```

## i3

I decided to give i3 a try, simply apt install it, then it shows up under the
gear icon at the login screen after a reboot.  At this point I don't think I am
ready for i3.  I have just changed a bunch of stuff in my workflow and honestly
I got a decent gnome config setup in like 10 minutes.

``` bash
sudo apt install i3
```
