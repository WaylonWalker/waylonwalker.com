---
templateKey: blog-post
tags: ['linux', 'bash']
title:  JUT | Read Notebooks in the Terminal
date: 2021-11-20T10:38:00
status: draft

---

Trying to read a .ipynb file without starting a jupyter server?  jut has you
covered.


## install

`jut` is packaged and available on pypi so installing is as easy as pip installing it.


``` bash
pip install jut
```

## examples


``` bash
jut https://cantera.org/examples/jupyter/thermo/flame_temperature.ipynb
jut https://cantera.org/examples/jupyter/thermo/flame_temperature.ipynb --head 3
jut https://cantera.org/examples/jupyter/thermo/flame_temperature.ipynb --tail 2
```

## what are all the commands available for jut?

Take a look at the help of the `jut` cli to explore all the options that it
offers.

``` bash
jut --help
```

There is some good information on the projects
[readme](https://github.com/kracekumar/jut/blob/main/requirements.txt) as well.

## without installing
_using pipx_

Don't want jut cluttering up your venv, or want to save yourself from making a
new one, [`pipx`](https://github.com/pypa/pipx) can manage a separate virual environment for you.  This is one
of the biggest selling points for me.

``` bash
pipx run jut https://cantera.org/examples/jupyter/thermo/flame_temperature.ipynb --head 3
```

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

### viewing markdown with glow

Glow is a terminal markdown viewer that looks really good.  These days I use
`bat` as `cat` so I don't get quite as much benefit from `glow`, but it still
looks pretty good.


```
glow flameflame_temperature.md
```

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

* [jut](https://github.com/kracekumar/jut/blob/main/requirements.txt)
* [nbconvert](https://nbconvert.readthedocs.io/en/latest/usage.html)
* [flame-temperature notebook](https://cantera.org/examples/jupyter/thermo/flame_temperature.ipynb)
* [glow](https://github.com/charmbracelet/glow)
* [lookatme](https://github.com/d0c-s4vage/lookatme)
* [pipx](https://github.com/pypa/pipx)
* [rich](https://github.com/willmcgugan/rich)
