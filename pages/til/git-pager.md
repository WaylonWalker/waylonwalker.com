---
date: 2022-03-16 14:03:18.294971
templateKey: til
title: Set Your Git Pager Config
tags:
  - git
  - cli

---

Setting up your git pager to your liking can help you navigate diffs and logs
much more efficiently.  You can set it to whatever pager you like so that your
keys feel nice and smooth and your fingers know exactly what to do.  You might
even gain a few extra features.

## Setting the pager

You can set the pager right from your command line with the following command.

``` bash
git config --global core.pager 'more'
```

You can also set your pager by editing your global `.gitconfig` file which by
default is set to `~/.gitconfig`.

``` bash
[core]
    pager = more
```

## Color

In my experience you need to turn colors off with nvim.  bat handles them and
looks good either way, but nvim will be plain white and display the color
codes as plain text if color is on.

``` bash
git config --global color.pager no
```

## Pagers I have tried

Here are some various configs that I tried.  For some reason line numbers in
bat really bothered me, but when in nvim they felt ok.  I am going to try
running both of them for a few days and see which I like better.  I think
having some of my nvim config could be really handy for things like yanking a
commit hash to the system clipboard without touching the mouse.

``` bash
# bat
git config --global core.pager 'bat'

# nvim in read only mode
git config --global core.pager 'nvim -R'

# turn colors off
git config --global color.pager no

# bat with no line numbers
git config --global core.pager 'bat --style=plain'

# nvim with no line numbers and a specific rc file
git config --global core.pager "nvim -R +'set nonumber norelativenumber' -u ~/.config/nvim/init-git.vim"
```

## reset back to the default

If you are afraid to try one of these settings, don't be you can always change
it back.  If you tried one and dont like it just `--unset` the config that you
just tried.

``` bash
git config --global --unset core.pager
git config --global --unset color.pager
```

The other option you have is to open your `.gitconfig` file and delete the
lines of config that set your pager.
