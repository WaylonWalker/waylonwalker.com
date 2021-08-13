---
Tags: ['cli', 'linux', 'tmux',]
templateKey: blog-post
title: tmux show-messages
date: 2021-08-14T09:03:09
status: published

---

https://youtu.be/LLk94fKpGg4

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


https://waylonwalker.com/tmux-nav-2021/

> for more information on how I navigate tmux, check out this full post

Also check out the full YouTube
[tmux-playlist](https://www.youtube.com/playlist?list=PLTRNG6WIHETB4reAxbWza3CZeP9KL6B)
to see all of the videos in this series.




