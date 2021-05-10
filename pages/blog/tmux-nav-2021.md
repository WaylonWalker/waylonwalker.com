---
templateKey: blog-post
tags: ['cli', 'linux']
title: How I navigate tmux in 2021
date: 2021-04-24T09:52:47
status: draft

---

<script>
change_speed = (speed) => [...document.querySelectorAll('video')].map(v => v.playbackRate=v.playbackRate+speed)
</script>
<style>
</style>

In 2021 I changed the way I navigate between tmux sessions big time.  Now I am
able to create, kill, switch with ease and generally keeping work separated
into logical groups.

## [Chris Toomey's](https://twitter.com/christoomey) Tmux Course

I took Chris's [tmux course](https://thoughtbot.com/upcase/tmux) in December
2020 and it was fantastic.  Even as a seasoned tmux user I learned quite a bit.
Prior to the course I was quite proficient in nagigating my tmux sessions, but
rarely started more than one session.  A few months later I have adopted a lot
of what I learned from Chris and made it my own.

> Prior to the course I was quite proficient in nagigating my tmux sessions, but
> rarely started more than one session.

### 📝 NOTE

Some of my config comes straight from the course, some of it has been extended to my liking.

<!-- ![overview of how I switch and manage tmux sessions](https://images.waylonwalker.com/tmux-navigation-2021.gif "overview") -->
<video controls muted autoplay playsinline loop=true width="100%">
    <source src="https://images.waylonwalker.com/tmux-navigation-2021.webm"
            type="video/webm">
    <source src="https://images.waylonwalker.com/tmux-navigation-2021.mp4"
            type="video/mp4">
    Sorry, your browser doesn't support embedded videos.
</video>

<div class='speed-control'>
    <button onclick="change_speed(.25)" >
        speed up
    </button>
    <button onclick="change_speed(-.25)" >
        slow down
    </button>
</div>

> Overview of how I navigate tmux

## ta

At the heart of my tmux navigation is a highly customized version of Chris's
tat script that I renamed `ta`.  Many folks add this to their bashrc `alias
ta=tmux attach`.  Simply calling ta will do the same thing as shown below.  If
your in a tmux session it does nothing, if your not in one it will attach you
to the first one.

<!-- ![overview of how I switch and manage tmux sessions](https://images.waylonwalker.com/tmux-navigation-2021-ta.gif "overview") -->
<video controls muted autoplay playsinline loop=true width="100%">
    <source src="https://images.waylonwalker.com/tmux-navigation-2021-ta.webm"
            type="video/webm">
    <source src="https://images.waylonwalker.com/tmux-navigation-2021-ta.mp4"
            type="video/mp4">
    Sorry, your browser doesn't support embedded videos.
</video>

<div class='speed-control'>
    <button onclick="change_speed(.25)" >
        speed up
    </button>
    <button onclick="change_speed(-.25)" >
        slow down
    </button>
</div>

> 👆 attaching to a session by default

In my `~/.bashrc` or `~/.zshrc` I add the ta command to automatically connect
to tmux.  Whenever I open my terminal I am automatically dropped into a tmux
session, but if I am opening a split within tmux It's smart enough to know not
to nest tmux sessions.

``` bash
ta
```

Another article can dive into my `ta` command, this one is more about the methodology, workflow, and keybinds to get me there.  It's available in my [devtainer repo](https://github.com/WaylonWalker/devtainer/blob/main/bin/ta).

### but theres more

Give it a directory and a `fzy` dropdown will let you choose a subdirectory to
start your session in, and name the session after that directory.

``` bash
ta ~/git
```

> 🔥 Bonus, use direnv to automatically set settings, echo your git status,
> activate your environment, or whatever else you need.

<!-- ![overview of how I switch and manage tmux sessions](https://images.waylonwalker.com/tmux-navigation-2021-ta-directory.gif "overview") -->
<video controls muted autoplay playsinline loop=true width="100%">
    <source src="https://images.waylonwalker.com/tmux-navigation-2021-ta-directory.webm"
            type="video/webm">
    <source src="https://images.waylonwalker.com/tmux-navigation-2021-ta-directory.mp4"
            type="video/mp4">
    Sorry, your browser doesn't support embedded videos.
</video>

<div class='speed-control'>
    <button onclick="change_speed(.25)" >
        speed up
    </button>
    <button onclick="change_speed(-.25)" >
        slow down
    </button>
</div>

> 👆 give it a directory, it will ask for input to which project and start a new
> named session in that directory.

Note that starting from outside currently does not start in a split layout like
it does when starting fromo within tmux.  I am still playing with this, but
generally I want my terminal session to be plain when I first start my
terminal.  Generally I am starting work after the first default session.


> 🤔  I still use both fzy and fzf, it probably doesn't make sense to use both,
> but I am currently giving fzy a try.

## prefix+w

_tmux choose-tree_

By default tmux comes with a `tmux choose-tree` command bound to `prefix+w`,
which opens in full screen.  The upper section of the screen will show every
window opened.  While selected you can show the splits in each window by
hitting l, or fold it with h. You can search for a session name by hitting /.

<!-- ![jump to existing sessions with prefix+w](https://images.waylonwalker.com/tmux-navigation-2021-prefix+w.gif "using prefix+w") -->
<video controls muted autoplay playsinline loop=true width="100%">
    <source src="https://images.waylonwalker.com/tmux-navigation-2021-prefix+w.webm"
            type="video/webm">
    <source src="https://images.waylonwalker.com/tmux-navigation-2021-prefix+w.mp4"
            type="video/mp4">
    Sorry, your browser doesn't support embedded videos.
</video>
<div class='speed-control'>
    <button onclick="change_speed(.25)" >
        speed up
    </button>
    <button onclick="change_speed(-.25)" >
        slow down
    </button>
</div>

``` bash
# ~/.tmux.conf

# expanded to show all splits
bind s choose-tree
# simpler window to show only sessions
bind S choose-session
```

### Keybindings in choose-tree/choose-session

| action | key |
|--------|-----|
| fold   | h   |
| unfold | l   |
| up     | k   |
| down   | j   |
| search | /   |

## prefix+c-w prefix+c-g

_open a project_

I setup to make it easy to open my non-work projects _(in my ~/git directory)_
and my work projects _(in my ~/work directory)_.  I bound `prefix+c-g` and
`prefix+c-w` to open a new session in their respecive directories.  I like
mapping common prefix commands with control so I can keep my pinky mashed on
that control key.

``` bash
# ~/.tmux.conf

bind C-w new-window -n "work-session-picker" "ta ~/work"
bind C-g new-window -n "git-session-picker" "ta ~/git"
```

<!-- ![create a new session from my ~/git directory](https://images.waylonwalker.com/tmux-navigation-2021-prefix+c-g.gif "using prefix+c-g") -->
<video controls muted autoplay playsinline loop=true width="100%">
    <source src="https://images.waylonwalker.com/tmux-navigation-2021-prefix+c-g.webm"
            type="video/webm">
    <source src="https://images.waylonwalker.com/tmux-navigation-2021-prefix+c-g.mp4"
            type="video/mp4">
    Sorry, your browser doesn't support embedded videos.
</video>
<div class='speed-control'>
    <button onclick="change_speed(.25)" >
        speed up
    </button>
    <button onclick="change_speed(-.25)" >
        slow down
    </button>
</div>

## prefix+c-j

_jump to session_

Now that I have `ta` rocking with a good create or attach setup I am rarely
toggling through a list of running sessions, but when I do I am doing it with
`prefix+c-j`. Thats keeping my finger on control and pressing `<space>+j`.
This keybinding uses fzf to fuzzy match to an existing session and attach.

``` bash
bind C-j new-window -n "session-switcher" "tmux list-sessions | sed -E 's/:.*$//' | grep -v \"^$(tmux display-message -p '#S')\$\" | fzf --reverse | xargs tmux switch-client -t"
```

<!-- ![jump to existing sessions with prefix+c-j](https://images.waylonwalker.com/tmux-navigation-2021-prefix+c-j.gif "using prefix+c-j") -->
<video controls muted autoplay playsinline loop=true width="100%">
    <source src="https://images.waylonwalker.com/tmux-navigation-2021-prefix+c-j.webm"
            type="video/webm">
    <source src="https://images.waylonwalker.com/tmux-navigation-2021-prefix+c-j.mp4"
            type="video/mp4">
    Sorry, your browser doesn't support embedded videos.
</video>
<div class='speed-control'>
    <button onclick="change_speed(.25)" >
        speed up
    </button>
    <button onclick="change_speed(-.25)" >
        slow down
    </button>
</div>

## M-N M-P

Next and Previous sessions.  This is super handy when working with under 3
sessions to be able to cycle through sessions holding `shift+alt` and pressing
`n` or `p`.

<!-- ![jump to next or previous sessions with m-N or m-P](https://images.waylonwalker.com/tmux-navigation-2021-m-N-M-P.gif "using m-N and m-P") -->
<video controls muted autoplay playsinline loop=true width="100%">
    <source src="https://images.waylonwalker.com/tmux-navigation-2021-m-N-M-P.webm"
            type="video/webm">
    <source src="https://images.waylonwalker.com/tmux-navigation-2021-m-N-M-P.mp4"
            type="video/mp4">
    Sorry, your browser doesn't support embedded videos.
</video>
<div class='speed-control'>
    <button onclick="change_speed(.25)" >
        speed up
    </button>
    <button onclick="change_speed(-.25)" >
        slow down
    </button>
</div>

## tkill

_time to clean up_

It's easy to get a long crufty list of sessions running throughout the day.
Typically this is not too bad on system resources compared to running vscode in
every working project, but it does make it more difficult to manage and wade
through the sessions list.  I use a handy shell alias, thats been in my zshrc
for quite some time.

``` bash
alias tkill="for s in \$(tmux list-sessions | awk '{print \$1}' | rg ':' -r '' | fzy); do tmux kill-session -t \$s; done;"
```

This is one that I don't have setup with a nice hotkey, but it works for my
fingers.  Most often I pop open a lower split(`M-s`), tkill, and close (`M-x`).


<!-- ![create a new session git-diff switch back to original session with prefix+c-g then use tkill to kill the git-diff session](https://images.waylonwalker.com/tmux-navigation-2021-tkill.gif "tkill example") -->
<video controls muted autoplay playsinline loop=true width="100%">
    <source src="https://images.waylonwalker.com/tmux-navigation-2021-tkill.webm"
            type="video/webm">
    <source src="https://images.waylonwalker.com/tmux-navigation-2021-tkill.mp4"
            type="video/mp4">
    Sorry, your browser doesn't support embedded videos.
</video>
<div class='speed-control'>
    <button onclick="change_speed(.25)" >
        speed up
    </button>
    <button onclick="change_speed(-.25)" >
        slow down
    </button>
</div>

## Last Session

_back_

While M-n and M-p work well with a small focused number of sessions, I often
end up with too many sessions open and its not efficient to remember a double
`M-N` followed by a tripple `M-P` to get back and fourth.  Most often I want to
get between two sessions very quick no matter what the order is.

``` bash
bind -n M-B switch-client -l
bind -n M-b switch-client -l
```

<video controls muted autoplay playsinline loop=true width="100%">
    <source src="https://images.waylonwalker.com/tmux-navigation-2021-m-b.webm"
            type="video/webm">
    <source src="https://images.waylonwalker.com/tmux-navigation-2021-m-b.mp4"
            type="video/mp4">
    Sorry, your browser doesn't support embedded videos.
</video>
<div class='speed-control'>
    <button onclick="change_speed(.25)" >
        speed up
    </button>
    <button onclick="change_speed(-.25)" >
        slow down
    </button>
</div>

> Once I get two sessions back to back I can switch between them with insane
> speed and precision.

## More Precision
_one keystroke_

The final layer of precision is for my most current projects that I need to get
to with a single keysroke.  These are bound to a set of keybindings that were
readily available, just above the home row.

``` bash
bind C-t new-session -A -s todo "cd ~/work/todo && nvim -O backlog.md doing.md done.md"
bind -n M-i new-session -A -s ww3 "cd ~/git/ww3/ && nvim"
bind -n M-o new-session -A -s images_waylonwalker_com "cd ~/git/images.waylonwalker.com/ && nvim"
```

<video controls muted autoplay playsinline loop=true width="100%">
    <source src="https://images.waylonwalker.com/tmux-navigation-2021-m-i-m-o.webm"
            type="video/webm">
    <source src="https://images.waylonwalker.com/tmux-navigation-2021-m-i-m-o.mp4"
            type="video/mp4">
    Sorry, your browser doesn't support embedded videos.
</video>
<div class='speed-control'>
    <button onclick="change_speed(.25)" >
        speed up
    </button>
    <button onclick="change_speed(-.25)" >
        slow down
    </button>
</div>

> These few directories are always at my fingertips encouraging me to keep better notes

And yes I did steal this last one from [Harpoon-man](https://twitter.com/ThePrimeagen) By The Way.


## Hub and Spoke
_M-i M-b_

I have really been digging this hub and spoke workflow where I am rocking away on a project hit `M-I`, take some notes
then hit `M-b` to get back to where I was.


![hub and spoke](https://images.waylonwalker.com/tmux-nav-hub-spoke.png)

> Model of my current workflow


---

Please let me know your thoughts
[@waylonwalker](https://twitter.com/_WaylonWalker), this one took me a bit
longer to put together with all of the animated gif's, but I think it helps
visually show how I navigate tmux everyday.

### Please give it a share if you liked it

If you liked it give share it and tag me on
[twitter](https://twitter.com/_WaylonWalker), I don't often ask but this one
took a bit more to put together than my normal post.

