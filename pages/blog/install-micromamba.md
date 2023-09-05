---
templateKey: blog-post
tags: ['bash', 'python']
title: How to Install micromamba on linux (from the comamnd line only)
date: 2021-04-21T13:32:27
published: true

---

I really like using conda (`miniconda`) as my python virtual environment
manager of choice.  It's simple and it includes its own python interpreter
using the version that I specify at creation.

## Mamba

_from their [readme](https://github.com/mamba-org/mamba)_

---

Mamba is a reimplementation of the conda package manager in C++.

* parallel downloading of repository data and package files using multi-threading
* libsolv for much faster dependency solving, a state of the art library used in the RPM package manager of Red Hat, Fedora and OpenSUSE
* core parts of mamba are implemented in C++ for maximum efficiency

At the same time, mamba utilize the same command line parser, package
installation and deinstallation code and transaction verification routines as
conda to stay as compatible as possible.

---


## Installing Micromamba

Similar to miniconda micromamba can be installed with a few lines of bash

``` bash
wget -qO- https://micromamba.snakepit.net/api/micromamba/linux-64/latest | tar -xvj bin/micromamba
./bin/micromamba shell init -s bash -p ~/micromamba
source ~/.bashrc
```

## Creating Environments with Micromamba

Creating new environments with micromamba is pretty similar to using conda.

``` bash
micromamba create -n mamba-new python=3.9 -y -c conda-forge
```

## -c is required

I was unable to figure out how to configure channels to `micromamba`, so I
needed to add `-c conda-forge` to my commands.


``` bash
                                           __
          __  ______ ___  ____ _____ ___  / /_  ____ _
         / / / / __ `__ \/ __ `/ __ `__ \/ __ \/ __ `/
        / /_/ / / / / / / /_/ / / / / / / /_/ / /_/ /
       / .___/_/ /_/ /_/\__,_/_/ /_/ /_/_.___/\__,_/
      /_/

WARNING No 'channels' specified
Encountered problems while solving:
  - nothing provides requested python 3.9**

ERROR   Could not solve for environment specs
```

> ⚠ micromamba thows this error when `-c conda-forge` is missing from the create command.

## Speed

micromamba is built for speed.  I tried it out in a replit.com session, while
it felt quite snappy creating a new environment was still within a few seconds
of conda on subsequent environment creations.  Their marketing says it should
be faster, but for what I use conda for I didn't see it.

## pip

I used conda install years ago while on windows machines struggling to compile
c-extensions and install certain troublesome packages, but I haven't used a
`conda install` in years, pip works just fine for my use.

## Useful Links

* GitHub: https://github.com/mamba-org/mamba
* Gitter: https://gitter.im/QuantStack/Lobby
* Documentation: https://mamba.readthedocs.io/en/latest/
