---
date: 2022-04-30 14:05:49
templateKey: blog-post
title: How I Quickly Capture Screenshots directly into My Blog
tags:
  - python
  - python
  - python
status: draft

---

When I am creating blog posts it's often helpful to add screenshots to them to
illustrate what I see on my screen.  Sometimes I lack good screenshots in my
posts because it just takes more effort than I have in the moment, and I
prioritize making content over making perfect content.

## Making Screenshots

When I have something to take a screenshot of, I need to take the shot,
optimize the image, often convert it to a better format, publish it, and
create a the img tag in my blog.

* take screenshot
* optimize
* conversion
* publish
* create img tag

## Created in 🐍Python

I created this tool for myself in python because that is what I am most
familiar with, but realistically most of what I am calling are shell scripts
that I could do in just about any language.

## Install my screenshot tool

My screenshot tool is quite hacky and not configurable, but works wonderfully
for me. If you like it and want to use it, make it configurable or fork it.
For now it lives on GitHub and since it has a setup.py with entrypoints we can
install it with pipx.

``` bash
pipx install git+https://github.com/WaylonWalker/screenshots.waylonwalker.com
```

> This is just a tool for me, it does not need to be in a package manager like pip.

## calling screenshot

Now that screenshot is installed we can call it and make a screenshot.  I'll
take a screenshot of the frontmatter of this exact post.

![screenshot-to-blog](https://screenshots.waylonwalker.com/screenshot-to-blog.webp)

I have this tool exposed as a command that can be ran in the command line by
calling `screenshot`.  I will rarely use it this way, but makes it easy to
create a hotkey for later.

## Success

Once the screenshot is successful, I get a `notify-send` message popup telling me so.

![screenshot-success](https://screenshots.waylonwalker.com/screenshot-success.webp)

## xbindkeys

Let's make this workflow just a bit smoother.  I want a desktop hotkey that I
can press at any time without opening a split or making sure I'm in zsh or vim,
I want it always there.  For hotkeys like this I use the Desktop manager
agnostic keybinding tool xbindkeys.  I can add the `screenshot` command and the
corresponding keybinding I want to my `~/.xbindkeysrc` file and restart with
`xbindkeys -f ~/.xbindkeysrc`.

```
"screenshot"
    Shift + Mod4 + alt + p
```

Now when I press `Shift + Mod4 + alt + p` I am presented with a little `zenity`
box asking me what I want to name my screenshot, followed by flameshot.

> xbindkeys allows me to bind this hotkey to my system so that no matter where
> I am it will work.

## Name it

The one question I ask myself when creating the hotkey is for a filename.  On
my ubuntu machine I do that with a simple gui application called zenity.  It
looks like this when I open it up.

![screenshot-zenity-window](https://screenshots.waylonwalker.com/screenshot-zenity-window.webp)

Under the hood my screenshot tool is running the following command in a subprocess.

```bash
zenity --entry --text="filename"
```
