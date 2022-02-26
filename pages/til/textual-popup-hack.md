---
date: 2022-02-26 15:41:12.156182
templateKey: til
title: Textual Popup Hack
tags:
  - python
  - cli
  - tmux

---

As I am toying around with textual, I am wanting some popup user input
to take over.  Textual is still pretty new and likely to change quite
significantly, so I don't want to overdo the work I put into it, So for
now on my personal tuis I am going to shell out to tmux.

## The Problem

The main issue is that when you are in a textual app, it kinda owns the
input.  So if you try to run another python function that calls for
`input` it just cant get there.  There is a
[textual-inputs](https://github.com/sirfuzzalot/textual-inputs) library
that covers this, and it might work really well for some use cases, but
many of my use cases have been for things that are pre-built like
copier, and I am trying to throw something together quick.

> textual is still very beta

Part of this comes down to the fact that textual is still very beta and
likely to change a lot, so all of the work I have done with it is for
quick and dirty, or fun side projects.

## The Solution

So the solution that was easiest for me... shell out to a tmux popup.
The application I am working on wants to create new documents using
copier templates.  copier has a fantastic cli that walks throught he
template variables and asks the user to fill them in, so I just shell
out to that with `Popen`.  Make sure that you wait for this process to
finish otherwise there will be bit of jank in your textual app.

``` python
async def action_new_post(self) -> None:
    proc = subprocess.Popen(
        'tmux popup "copier copy plugins/todo-template tasks"', shell=True
    )
    proc.wait()
```

## example

Here is what the running todo application looks like with the copier
popup over it.

![example of the popup running over textual](https://images.waylonwalker.com/textual-popup-hack.png)

https://waylonwalker.com/tmux-popups/

> a bit more on tmux-popus [here] https://waylonwalker.com/tmux-popups/)

## Links

* [textual repo](https://github.com/Textualize/textual/)
* [textual-inputs repo](https://github.com/sirfuzzalot/textual-inputs)
* [my article on tmux popups](https://waylonwalker.com/tmux-popups/)
