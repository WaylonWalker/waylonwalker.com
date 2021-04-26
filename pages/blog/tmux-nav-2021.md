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
.speed-control {
    display: flex;
    flex-direction: row;
    justify-content: center;
    margin-top: -1rem;
    padding: 1rem 0 .5rem;
    background: rgba(0,0,0, .3);
    pause-before:
}
.speed-control button {
    margin: .4;
    transition: all 0.2s;
    border: .1rem solid #d3d3d3;
    color: #d3d3d3;
    background: none;
    text-align: center;
    padding: .35rem 1.2rem;
    margin: .1rem .5rem;
    border-radius: .12rem;
}
.speed-control button:hover {
    color: black;
    background: #d3d3d3;
}
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

### but theres more
_give it a directory_

passing in a 

## prefix+w

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

## prefix+c-w prefix+c-g

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
