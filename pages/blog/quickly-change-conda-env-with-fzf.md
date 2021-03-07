---
templateKey: blog-post
tags: ['python']
title: Quickly Change Conda Env With Fzf
date: 2021-01-11T00:00:00
status: published

---

Changing conda environments is a bit verbose, I use a function with fzf that
both lists environments and selects the one I want in one go.

## Conda

I have used conda as a virtual environment tool for years now.  I started using
conda for its simplicity to install packages on windows, but now that has
gotten so much better and it's been years since I have run a `conda install`
command.  I'm sure that I could use a different environment manager, but it
works for me and makes sense.

> What environment manager do you use for python?

Conda environments are stored in a central location such as
`~/miniconda3/envs/` and not with the project.  They contain both the python
interpreter and packages for that env.

## Conda create

Conda environments are created with the `conda create` command.  At this point,
you will need to name your env and select the python version.

``` bash
conda create -n my_env python=3.8
```

After running this command you will have a directory `~/miniconda3/envs/my_env`
with a base python install.  It will not be active yet.

## List environments

Before activating an environment I often want to list the environments that I
have installed which are often upwards of 70, so it's hard to remember them
all.

``` bash
conda info --envs
```

After running this command you will see something like the following.

``` bash
# conda environments:
#
base                     /home/waylon/miniconda3
my_env                   /home/waylon/my_env
```

## Activating an environment

Activating a conda environment will do some magic to your current shells
`$PATH` variable to ensure that the environment that you select is preferred
over the base environment.

``` bash
conda activate my_env
```

## Ready to work

Now you can install packages for your project in an isolated environment safe
from wrecking another project or being wrecked by another project.

``` bash
pip install -r requirements.txt
```

## Using fzf

_a bit less verbose_

[fzf](https://github.com/junegunn/fzf) is an amazing tool for the terminal that
is a generic fuzzy matcher.  It is super performant and can handle insane
amounts of text and is brilliant at figuring out what you mean with just a few
characters.  We can use it here to list out all of our conda environments and
select the one we want to activate with just a few keystrokes.

### Selecting the environment.

Piping our list of environments directly into `fzf` gives us a fuzzy selection
where we can type a few characters and it will return the row we were looking
for.

``` bash
conda info --envs | fzf
```

This returns us something like this which also includes the path where it is
located.

``` bash
my_env                 /home/walkews/miniconda3/envs/my_env
```

### getting just the environment name

To get just the name without the path I pipe the output into awk.  There are
many ways to do this in bash, this is the way that worked for me at the time I
made this function.

``` bash
conda info --envs | fzf | awk '{print $1}'
```

### Time to activate

Functions that use `fzf` can be a bit odd, running them in a subshell with the
$() syntax generally makes it super simple to utilize the output.  No matter
how many times I have tried without running it in a subshell it's always buggy
without it.

``` bash
conda activate "$(conda info --envs | fzf | awk '{print $1}')"
```

This will now run conda activate on the environment that we select with fzf.

### Make it a function

We don't want to type that out every time we want to activate an environment. I
keep a function called `a` in my `~/.bashrc` and `~/.zshrc` so that I can
activate an environment with a single character.  Yes, I switch environments
often enough to justify the valuable namespace of a single character.

``` bash
a () {
  conda activate "$(conda info --envs | fzf | awk '{print $1}')"
}
```

https://waylonwalker.com/reusable-bash

> for more information on writing reusable bash scripts check out one of my
> favorite articles

I am always on the lookout for cool new use cases for `fzf`, if you have one please share it with me.


