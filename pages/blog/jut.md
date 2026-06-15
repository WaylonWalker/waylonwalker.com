---
templateKey: blog-post
tags: ['linux', 'bash', 'datascience']
title:  JUT | Read Notebooks in the Terminal
date: 2021-11-20T10:38:00
published: true

---

Trying to read a .ipynb file without starting a jupyter server?  jut has you
covered.

https://youtu.be/t8AvImnwor0

> watch the video version of this post on [YouTube](https://youtu.be/t8AvImnwor0)

![57676ca9-23dd-4b3d-a084-293a0525eba5.mkv](https://dropper.wayl.one/file/57676ca9-23dd-4b3d-a084-293a0525eba5.mkv)
Or watch the full thing here

## install

`jut` is packaged and available on pypi so installing is as easy as pip installing it.


``` bash
pip install jut
```

![installing jut with pip](https://dropper.wayl.one/file/f7db3e0e-cc41-44f2-b410-8e7bc5fe1a58.mp4)

> ! This is my first time including snippets of the video in the article like this, let me know what you think!

## examples


``` bash
jut https://cantera.org/examples/jupyter/thermo/flame_temperature.ipynb
jut https://cantera.org/examples/jupyter/thermo/flame_temperature.ipynb --head 3
jut https://cantera.org/examples/jupyter/thermo/flame_temperature.ipynb --tail 2
```

![running jut examples](https://dropper.wayl.one/file/08743803-99cc-4881-831d-6ef17d8c1065.mp4)

## what are all the commands available for jut?

Take a look at the help of the `jut` cli to explore all the options that it
offers.

``` bash
jut --help
```

There is some good information on the projects
[readme](https://github.com/kracekumar/jut) as well.

![getting help with jut](https://dropper.wayl.one/file/ba21e724-3fff-4320-8fb9-4fe62442aab2.mp4)

## without installing
_using pipx_

Don't want jut cluttering up your venv, or want to save yourself from making a
new one, [`pipx`](https://github.com/pypa/pipx) can manage a separate virual
environment for you.  This is one of the biggest selling points for me.

``` bash
pipx run jut https://cantera.org/examples/jupyter/thermo/flame_temperature.ipynb --head 3
```

![running jut with pipx](https://dropper.wayl.one/file/d4399ec7-9046-4cbe-b1cb-4a453be8bf4b.webm)

## nbconvert

`jut` is the lightweight option that I think will fit the bill often for me,
but it just doesn't always cut it.  Mostly if there are images in the notebook
or  large output that is hard to read, its time to pull out the medium guns
that sit between fulling running jupyter and `jut`.

``` bash
pip install nbconvert
```

> nbconvert does not have its own cli, instead it sits under the jupyter command.


### converting to html

> Need to see images, go here!

``` bash
wget https://cantera.org/examples/jupyter/thermo/flame_temperature.ipynb
jupyter nbconvert flame_temperature.ipynb --to html
python -m http.server
```

> Note, nb convert does not work with a url, you will need to have the notebook locally.

![nbconvert to html to see images](https://dropper.wayl.one/file/7a3087f4-dd03-46f9-ad23-8ed655b14849.webm)

## what other options does nbconvert offer?

`nbconvert` also offers a standard help flag that you can access by passing in
the `--help` flag

``` bash
jupyter nbconvert --help
```

### converting to markdown

`nbconvert` also supports converting to many other formats, one option that is
quite interesting for use in the terminal is markdown.  We could simply convert
the notebook to markdown and cat it out.

``` bash
jupyter nbconvert flame_temperature.ipynb --to maarkdown
cat flameflame_temperature.md
```

![nbconvert to markdown and displaying in bat](https://dropper.wayl.one/file/bf2e3759-9d61-40df-9945-feaf28333e16.mp4)

### viewing markdown with glow

Glow is a terminal markdown viewer that looks really good.  These days I use
`bat` as `cat` so I don't get quite as much benefit from `glow`, but it still
looks pretty good.


```
glow flameflame_temperature.md
```

![nbconvert to markdown and displaying in glow](https://dropper.wayl.one/file/341a0a28-dd3b-46c4-b6f6-a5aeef78e5eb.mp4)

### viewing markdown as slides with lookatme
_[lookatme](https://github.com/d0c-s4vage/lookatme)_

Lookatme is my slideshow tool of choice.  Creating slides in markdown is such a
fantasic user experience,  It realy lets you go from outline to finished slide
deck fluidly.  Refactoring the whole thing is also so much easier than with gui
tools.  Once you have your idea fleshed out it does make the process of making
slides in powerpoint much easier if thats what you need.


On to nbconvert, without even changing the notebook we can look at the notebook
as a slideshow in the terminal.  The only thing that it needs is some markdown
headers to start new slides from.

``` bash
lookatme flameflame_temperature.md
```

![nbconvert to markdown and displaying as slides with lookatme](https://dropper.wayl.one/file/1aaca40c-883f-4013-8dd9-c7db3b8a46b4.mp4)

### viewing markdown with rich

Bringing this full circle, lets take a look at the converted markdown with
rich.  Here you will notice a surprising similarity to what we saw with `jut`.

``` bash
pip install rich
python -m rich.markdown flame_temperature.md
```

Rich still cannot pull directly from a url or display markdown with out being
installed and managed by yourself.  Unlike how `jut` can leverage [`pipx`](https://github.com/pypa/pipx) to
manage the installation sandbox for you.



## Links

* [jut](https://github.com/kracekumar/jut) - View notebooks in the terminal
* [nbconvert](https://nbconvert.readthedocs.io/en/latest/usage.html) - convert notebooks to other formats
* [flame-temperature notebook](https://cantera.org/examples/jupyter/thermo/flame_temperature.ipynb) - The sample notebook I used
* [glow](https://github.com/charmbracelet/glow) - Terminal Markdown viewer
* [lookatme](https://github.com/d0c-s4vage/lookatme) - Terminal Markdown slideshow tool
* [pipx](https://github.com/pypa/pipx) - Run python cli's without maintianing a virtual environment
* [rich](https://github.com/willmcgugan/rich) - Beautiful python terminal formatter
