---
date: 2025-07-06 12:37:40
templateKey: blog-post
title: command palettes are overrated
tags:
  - dev
published: True

---

Command palettes are slow, and overrated, you should treat yourself better.
You probably installed VSC*** out of the box and your co-workers see you using
the mouse and reprimanded you as they should.  Mouse usage is not OK if you are
a software dev, you should have the cheap ass free mouse that came with your
cousins dell machine five years ago and only use if for emergencies.  If you
want to be fast you cannot do that by moving cursors to imprecise locations and
clicking with your hand.  You are not a caveman, put down the stones and get
with the damn times.  You need to be moving with precision.

## Stage One, the command palette

So you are taking your first few baby steps away from that Logitech MX Master
and you need to get shit done, during these infant months the command palette
is your friend.  Use it you will be 10x faster than Razer Naga Ron from
accounting.  If you are in an IDE like `VSC***` or a JEttedBrains editor they
come with a command palette for running commands and fuzy finding files, use
it.  If you are in nvim, move on you probably don't need this, unless you are
still teething on `VSC***`, during that tim use `:Telescope commands`.

## Close the fn Tree

You don't need a goddamn file tree open all the goddamn time, its taking up
screen space and filling your brain with useless shit.  They can be a helpful
tool to move, rename, refactor files, or familiarize yourself with a codebase,
but you don't use one if you want to walk someday, so just like the command
palette we are going to give it up for fuzzy find.  If you are in nvim you are
going to want to use `:Telescope find_files`  those other big brained ides have
things, look up the keybinding.

## Now that we are crawling

As you start to get your legs under you and you can crawl away from mamas teet
note down the commands that you use all the time, we want to get command
palette usage way down.  Not to zero, without some sort of fuzzy command picker
(even `:<tab>`) you are probably trying to remember too much and allocating too
many brain cells to editing text, don't do that.  Resist over-correcting.

## assign hotkeys

Now you need to get yourself some hotkeys going, this is for the hot shit that
you use several times a minute.  You should be able to do things like swap
between the current file and the last file in one keystroke without wasting a
single brain cycle, it should be automatic.  Go to definition, go to reference,
no searching, searching is slow, find_files is slow.  These are tools for
exploration we are tyring to get real work done here.

Here's a few things you should be able to do if you want to keep up with your
Grandma, she's been slayin these keys for years.

* go to definition
* go to reference
* find_files
* find and replace
* rename
* git add this file, commit, push
* go to the last file
* go up and down the jumplist
* go up and down the quickfix list
* list open files
* harpoon all the files you go to regularly
* format
* move around your files

## fly

Over time you should be using your command pallete less and less, this is not
designed to run every goddamn command through.  Note the ones you use a lot and
add keybinds.  If you are using one of those editors that don't make it clear
what the fuck your running when you execute a command ask gippity, it can
probably knock out that binding in 30s just fine.

## inspiration

The decline of "vim btw" by Sylvan Franklin.  It's a pretty incredible video,
he is crushing these half satire dry humor tech content videos.  He nails that
with the death of vimBTW we lost the craft of knowing your editor in and out.
We lost the art of flying through text.  Now we have plugin kitties that say
vimBtw, but they really aren't using any vim features past hjkl.

[[ thoughts-724 ]]

<https://www.youtube.com/watch?v=RmnqdAidVeE>
