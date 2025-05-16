---
date: 2025-05-16 08:24:51
templateKey: til
title: vhs themes
published: true
tags:
  - tui
  - vhs
  - terminal

---


I've been working on
[ninesui](https://github.com/WaylonWalker/ninesui/blob/main/README.md),
inspired by k9s see [thoughts-633](https://thoughts.waylonwalker.com/post/633).
I want a good flow for making video for the readme and I am using [char.sh](https://charm.sh/apps/)'s [vhs](https://github.com/charmbracelet/vhs) for this.
Its running in an archBTW distrobox and looks gawdaweful.

![sort.mp4](https://dropper.wayl.one/api/file/e86047ed-6881-43f7-8e3a-30411d51afaf.mp4)

The over saturated colors give it a really retro look, seems fine, but not my
cup of tea.  I tried to change the textual theme to `tokyo-night` and it might
have made it a bit better, but still over-saturated.

## After

What I found is that vhs has themes, setting it to `dracula` made everything much better.

``` diff
# sort.tape
Output assets/sort.mp4
Output assets/sort.gif

Require echo

Set Shell "bash"
Set FontSize 32
Set Width 1920
Set Height 1080
+ Set Theme 'Dracula'
```

![sort.mp4](https://dropper.wayl.one/api/file/ada8f04d-88ac-41c3-9983-d9e849cc13ad.mp4)
