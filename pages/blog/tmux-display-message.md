---
Tags: ['cli', 'linux', 'tmux',]
templateKey: blog-post
title: tmux display-message
date: 2021-08-12T09:03:09
published: true

---

https://youtu.be/utfLA6L8o5s

You've got some long running tasks, and you're trying to stay productive and
knock tasks off that board, but you keep finding that your processes finish and
you stay on other tasks for longer than you should.  You were in the flow and
just did not check back in on it.  With `display-message` you can send yourself
a notification when that long running task is complete.

## from the man page

Here is a snippet of `display-message` from the tmux man page.  I rarely need
to do anything other than just display message, but there are other flags for
it.

``` bash
display-message [-aINpv] [-c target-client] [-d delay] [-t target-pane] [message]
            (alias: display)

        Display a message.  If -p is given, the output is printed to stdout,
        otherwise it is displayed in the target-client status line for up to

        delay milliseconds.  If delay is not given, the message-time option is
        used; a delay of zero waits for a key press.  ‘N’ ignores key presses
        and closes only after the delay expires.  The format of message is
        described in the FORMATS section;

        information is taken from target-pane if -t is given, otherwise the
        active pane.

        -v prints verbose logging as the format is parsed and -a lists the
        format variables and their values.

        -I forwards any input read from stdin to the empty pane given by
        target-pane.
```

## notifier

With `display-message` we can do things like setup notifications that will work
cross platform.

``` bash
cmatrix -t 5 && tmux display-message done
```

Without setting the target-pane `display-message` defaults to the active pane.
This is a very handy feature that allows us to switch windows, or sessions and
still recieve the message.


https://waylonwalker.com/tmux-nav-2021/

> for more information on how I navigate tmux, check out this full post


Also check out the full YouTube
[tmux-playlist](https://www.youtube.com/playlist?list=PLTRNG6WIHETB4reAxbWza3CZeP9KL6Bkr)
to see all of the videos in this series.
