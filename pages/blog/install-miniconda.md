---
templateKey: blog-post
related_post_label: Check out this related post
tags: ['bash', 'python']
title: How to Install miniconda on linux (from the command line only)
date: 2020-08-10T05:00:00Z
status: published
description: Installing miniconda from only the command line can be a bit of
    an intimidating task your first time. Lets walk through how to do it.
cover: '/static/install-miniconda.png'

---

miniconda is a python distribution from continuum. It's a slimmed-down version of their very popular anaconda distribution. It comes with its own environment manager and has eased the install process for many that do not have a way to compile c-extensions. It made it much easier to install the data science stack on windows a few years ago. These days windows are much better than it was back then at compiling c-extensions. I still like its environment manager, which installs to a global directory rather than a local directory for your project.

## Installing miniconda on Linux

Installing miniconda on Linux can be a bit tricky the first time you do it completely from the terminal. The following snippet will create a directory to install miniconda into, download the latest python 3 based install script for Linux 64 bit, run the install script, delete the install script, then add a conda initialize to your bash or zsh shell. After doing this you can restart your shell and conda will be ready to go.

``` bash
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh
```

## Options

The miniconda.sh script comes with a few basic options.  Most notably we used `-b` to be able to run unattended, which means that all of the agreements are automatically accepted without user prompt.  `-u` updates any existing installation in the directory of install if there is one. `-p` is the directory to install into.

```
usage: /root/miniconda3/miniconda.sh [options]

Installs Miniconda3 4.6.14

-b           run install in batch mode (without manual intervention),
             it is expected the license terms are agreed upon
-f           no error if install prefix already exists
-h           print this help message and exit
-p PREFIX    install prefix, defaults to /root/miniconda3, must not contain spaces.
-s           skip running pre/post-link/install scripts
-u           update an existing installation
-t           run package tests after installation (may install conda-build)
```


## Silent/Logged

A quick and easy way to silence everything or to log it to a file during an automated install is to wrap the script into a bash function, or save it to its own file, and call the file.  I like the function method since I can still copy it right into a terminal, or keep my install script as one single file.

``` bash
install_miniconda () {
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh
}
```

**normal**
```
install_miniconda
```

**silent**
```
install_miniconda > /dev/null 2>&1
```

**logged**
```
install_miniconda > miniconda_install.log 2>&1
```

https://waylonwalker.com/reusable-bash/

> This posts covers more ways to write reuable bash scripts

## Cross posted to DEV

Check out this post and many more on [dev.to/waylonwalker](https://dev.to/waylonwalker/installing-miniconda-on-linux-from-the-command-line-4ad7)
