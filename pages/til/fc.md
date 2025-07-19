---
date: 2025-07-18 07:52:53
templateKey: til
title: fc
published: true
tags:
  - linux
  - bash

---

I am a linux user through and through.  Desktop, server, vms, containers,
everything except my phone is linux.  With this I spend a lot of time in the
terminal, and have been a long time user of `!!` to rerun the last command, but
with the ability to tack something on at the beginning or end.

TIL about `fc`, which opens the last command in your shell history in your
`$EDITOR` or pass in your editor `-e nvim`.

[man fc](https://manned.org/fc)

## Rcap of how !! works

`!!` pronounces `bang bang` and will run the last command in your history.

``` bash
ls -l

!! | wc -l
# ls -l | wc -l

sudo !!
# sudo ls -l | wc -l

!!:s/-l/-l \/tmp
# sudo ls -l /tmp | wc -l
```

## `fc` enters the chat

Now making complex edits in your shell can be a bit of a chore, so `fc` moves
this work to your `$EDITOR`.

``` bash
fc
```

This pops open your $EDITOR with the last command in your history.

``` vim
sudo ls -l | wc -l
```

![screenshot-2025-07-18T13-21-46-775Z.png](https://dropper.wayl.one/api/file/9d624d65-de40-459b-9566-6e5c833cabcc.png)

## Shell History

`fc` shows up in shell history, but `!!` does not, `!!` gets replaced by the
command that it becomes.

## Up Arrow

yaya yaya, I know you can also `up-arrow c-e`, but what fun is that, it's barely a
flex.  `fc` just looks big brained and like you really know what you are doing.
