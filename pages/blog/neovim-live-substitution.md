---
templateKey: blog-post
tags: 
  - linux
  - vim
title: Live Substitution In Neovim
date: 2021-01-04T00:00:00
status: published
description: ''
cover: "/static/neovim-live-substitution.png"

---

Replacing text in vim can be quite frustrating especially since it doesn't have
live feedback to what is changing. Today I was watching Josh Branchaud's
Vim-Unalphabet series on Youtuve and realized that his vim was doing this and I
had to have it.

https://twitter.com/_WaylonWalker/status/1346081617199198210


## How to do it.

I had to do a bit of searching and found a great post from [vimcasts](http://vimcasts.org/episodes/neovim-eyecandy/) that shows exactly how to get the live search and replace highlighting using `inccomand`


## :h inccommand


``` vim
'inccommand' 'icm'	string	(default "")
			global
			
	"nosplit": Shows the effects of a command incrementally, as you type.
	"split"	 : Also shows partial off-screen results in a preview window.

	Works for |:substitute|, |:smagic|, |:snomagic|. |hl-Substitute|

	If the preview is too slow (exceeds 'redrawtime') then 'inccommand' is
	automatically disabled until |Command-line-mode| is done.

```

## Add this to your config

I believe that this is a neovim only feature, add it into your
`~/.config/nvim/init.vim` file. You can see it in my
[dotfiles](https://github.com/WaylonWalker/devtainer/blob/main/dotfiles/.config/nvim/settings.vim#L155)
as well.

``` vim
set inccommand=nosplit
```

## See it in Action

![example live
substitution](https://waylonwalker.com/nvim-live-substitute-inccommand.gif)

## The Video that inspired this

Check out Josh Branchaud's great series on the Vim-Unalphabet.

https://www.youtube.com/watch?v=5jMiYtXz2QA
