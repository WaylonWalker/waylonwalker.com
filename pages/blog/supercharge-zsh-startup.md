---
templateKey: blog-post
tags: ['bash', 'linux']
title: Supercharge Zsh Startup
date: 2020-01-03T06:00:00.000+00:00
status: published

---

I have been using oh-my-zsh successfully for about 2 years now. But lately my startup time has been really bothersome. It has grown to the point where it was taking about **5.5s** to startup a shell!  This is ok if I am going to spend some time in here for awhile and do some work that benefits from all of the autocompletions, plugins, and shortcuts that oh-my-zsh brings.  But to only jump in to run a handful of commands is infuriating.

### 📑 My Setup

I believe the real issue is io speed on wsl.  I have some remote servers with similar configs that are 10x faster or more, loading in 100s of milliseconds rather than seconds.  Sourcing all of the individual plugin files are just too much for it.

## 💨 How Fast can it be

> Quick side note: your zsh config is controled by your \~/.zshrc file.  This file can source other files, load plugins, or run literally anything.

Time the **initial** time

``` bash
time zsh -c exit
```

Move your **\~/.zshrc** config file.

``` bash
mv ~/.zshrc ~/.zshrc-back
```

Time the fastest startup possible with nothing in your **\~/.zshrc** config file.

``` bash
time zsh -c exit
```

Move your **\~/.zshrc** back

``` bash
mv ~/.zshrc-back ~/.zshrc
```

## 🕵️‍♂️Profile your startup time

It is possible to profile your zsh startup time by adding `zmodload zsh/zprof` to the start of your `~/.zshrc` file and `zprof` at the end.  This was unsuccessfull for me.  I ended up just backing up `~/.zshrc` file, then deleting half of it to see where the hot spots were.  I found that two places that were really hot for me.  One I was inadvertantly setting git and npm settings everytime that didnt need to be set everytime.  That was an easy 2s gain.  Another easy 3s gain was removing oh-my-zsh.

``` bash
# ~/.zshrc
zmodload zsh/zprof
...
..
.
zprof
```

## 😭But I really like oh-my-zsh

without all the bells and whistle that oh-my-zsh provided zsh became lightning fast to load, but incredibly boring.  It was also very painful to manually type out everything that it autocompleted or aliased all the time.  Next I headed down a path to get all of that functionality back without sacrificing load time.

> Without oh-my-zsh, zsh became incredibly boring.

## 🔌 Plugin Managers

![](https://images.waylonwalker.com/static/steve-johnson-ZUabNmumOcA-unsplash.jpg)

> Photo by [Steve Johnson](https://unsplash.com/@steve_j?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/plug?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

* oh-my-zsh
* zplugin
* zgen

There are a number of plugin managers for zsh, I tried each of the ones listed above, but found that as I approached a nice setup that I liked the load time would creep up **above the 2s** **mark** each time. I would turn certain plugins on and off, try different plugin managers, before realizing that I had spent enough time on this problem and it was going to be time to settle on fast startup or functionality.

## ⚖ Finding Balance

_Semi-lazy loading_

![](https://images.waylonwalker.com/static/jeppe-hove-jensen-b3eaH1hguOA-unsplash.jpg)

> Photo by Jeppe Hove Jensen on [Unsplash](https://unsplash.com/s/photos/balance?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

After struggling to get all of the features I wanted with a fast load time, I decided to only load what I needed upon startup.  Next I created a simple alias that loads in zgen and all of the plugins I want. By doing this I get two main benefits.  Obviously I get a faster starup time by loading less.  I got my startup time down to about 0.25s.

``` bash
# ~/.zshrc
p () {
zgen load zsh-users/zsh-autosuggestions
....
..
.
}
```

### ⚡ Fast Loading

I really like the fast startup time, because sometimes I am only loading up zsh to run a handful of commands that dont need much in the way of plugins

**simple commands that need 💨 blazing start speed**

_any single easy to type command, these are my common commands that I will open a terminal in my editor and just need to run quick._

* vim
* git add . && git commit && git push
* sh my_script.sh
* make build
* bake build
* pytest
* gatsby develop
* npm i
* npm update
* pip install
* ipython

The second benefit was that I can continue typing while plugins are loading.

![](/static/type-while-loading-plugins.gif)

## >Prompt

After removing oh-my-zsh the first thing that I missed was the themes that it provided.  I went through a number of them and the one that seemed to have the smallest effect on performance and everything I needed was [starship](https://starship.rs/).  It's a really fast prompt written in rust.  The biggest thing that I needed to have that other prompts were misssing was conda environments.  I live much of my work life running python from various conda environments and it is crutial that I can see what environment I am in at all times.

![](https://images.waylonwalker.com/2020-01-04 12-36-31_Cortana.png)

## 💰 Bonus

I applied the same logic to neovim and achieved similar results.  Again it just had too many plugins loading on startup for simple tasks.  I ended up taking a shortcut and load any heavy plugins upon NerdTreeToggle.  I dont really use NERDTree that much, but when I do its for more than just a quick edit.

``` bash
# ~/.config/nvim/init.vim
Plug 'valloric/youcompleteme', {'do': './install.py', 'on': 'NERDTreeToggle'}

```
