---
templateKey: blog-post
title: Bash
date: 2019-09-08T05:00:00.000+00:00
status: published
description: Waylon Walker's Bash Notes
cover: "/static/hannah-gibbs-BINLgyrG_fI-unsplash.jpg"
tags:
- python
- cli

---
# Bash Notes

Bash is super powerful.

## File System Full

**Show Remaining Space on Drives**

```bash
df -h
```

**show largest files in current directory**

```bash
du . -h --max-depth=1
```

**Move files then symlink them**

``` bash
mkdir /mnt/mounted_drive
mv ~/bigdir /mnt/mounted_drive
ln -s /mnt/mounted_drive/bigdir ~/bigdir
```

## Fuzzy One Liners

```bash
a() {source activate "$(conda info --envs | fzf | awk '{print $
```

**edit in vim**

```bash
vf() { fzf | xargs -r -I % $EDITOR % ;}
```

**cat a file**

```bash
vf() { fzf | xargs -r -I % $EDITOR % ;}
```

**bash execute**

```bash
bf() { bash "$(fzf)" }
```

**git add**

```bash
gadd() { git status -s | fzf -m | awk '{print $2}' | xargs git add && git status -s}
```

**git reset**

```bash
greset() { git status -s |  fzf -m | awk '{print $2}' |xargs git reset && git status -s}
```

**Kill a process**

```bash
fkill() {kill $(ps aux | fzf | awk '{print($2)}')}
```

## Finding things

### Files

[fd-find](https://github.com/sharkdp/fd) is amazing for finding files, it even respects your `.gitignore` file 😲.  Install with `apt install fd-find`.

```bash
fd md
```

```bash
ag -g python
```

```bash
find . -n "*.md"
```

_++Vanilla Bonus_

### Content

\** show matching text **

```bash
ag python
```

```bash
grep -iR Python
```

_++Vanilla Bonus_

\** show file names only **

```bash
ag -l python
```

```bash
grep -iRl python
```

_++Vanilla Bonus_

### Recursively Replace text

```bash
agr() {ag -l "$1" | xargs sed -i "s/$1/$2/g"}
```

_++Vanilla Bonus_

```bash
grepr() {grep -iRl "$1" | xargs sed -i "s/$1/$2/g"}
```

**Extending** `**agr**` **or** `**grepr**`

There are so many options inside of `grep`, `ag`, and `sed` that you could many an enormous amount of these if you really wanted to, but I like to keep it simple.  These cover 90% of my usage.  If I wanted to change something in the second half I would just paste in this command and edit it. More often though I want to limit the input, say only replace word1 to word2 inside of markdown files.

**Limited Scope**

```bash
fd md | xargs argr python python3
```

```bash
find . -n "*.md" | xargs grepr python python3
```

_++Vanilla Bonus_


https://waylonwalker.com/refactor-in-cli


> I use these replace commands heavily when doing large refactorings.

### conditionally configure

I like this one when there is not a good cli into config files and I need to replace something like a true to false if the value is in the config and append to the config if its not.

``` bash
grepr() {
    # replaces first string with second string inside file from third argument
    # example:
    #   grepr "allow_conda_downgrades:.*" "allow_conda_downgrades: true" ~/.condarc
    if grep -xq $1 $3
    then
        sed -i "s|$1|$2|g" $3
    else
        echo "$2" >> $3
    fi
}
```

### Watch the time

``` bash
watch -n 1 date
```

_++Vanilla Bonus_

**with figlet**

``` bash
watch -n 1 bash -c "date | figlet"
```

### watch a function

``` bash
run () {
date
aws s3 sync $BUCKET .
}
export -f run
watch -n 10 run
```

### if conda environment does not exist create it

``` bash
conda info --envs | grep my_env && echo "my_env environment is installed" || conda create -n my_env python=3.8 -y
source activate my_env
```

# Rename multiple files

more info from [linuxize](https://linuxize.com/post/how-to-rename-files-in-linux/)

``` bash
for f in *.png; do
   mv ${f} prefix-${f}
done
```

## convert all files in a directory to unix

``` bash
dos2unix **/*
```

## recursively remove all whitespace from .py files

``` bash
find **/*.py -type f -exec sed -i 's/ *$//' '{}' ';'
```

## recursively autopep8

``` python
find . -name '*.py' -exec autopep8 --in-place '{}' \;
```

## make bash script a runnable command

include a shebang

``` bash
#! /bin/bash
```

chmod

``` bash
chmod +x /usr/local/bin/my_script
```

accept positional input

``` bash
#! /bin/bash
input=$1
echo input
```

# Using pyp

``` bash
pipx install pyp
```

## replacement for cut

``` bash
❯ python -m http.server 5000 &
[1] 8574

✦ ❯ Serving HTTP on 0.0.0.0 port 5000 (http://0.0.0.0:5000/) ...

✦ ❯ ps aux | grep "python -m http.server" | grep -v grep | pyp 'line.split()[1]' | xargs kill
[1]  + terminated  python -m http.server 5000
```

## replacement for wc

``` bash
conda info --envs | pyp 'len(lines) - 3 # account for header and base'
```

## print contents of shell function

``` bash
declare -f <function-name>
```

## batch rename files

``` bash
for f in *.jpeg; do
    mv -- "$f" "${f%.jpeg}.jpg"
done
```

## convert markdown files to reveal.js

https://github.com/jgm/pandoc/wiki/Using-pandoc-to-produce-reveal.js-slides
install pandoc

``` bash
apt install pandoc
```

setup

``` bash
wget https://github.com/hakimel/reveal.js/archive/master.tar.gz
tar -xzvf master.tar.gz
mv reveal.js-master reveal.js
```

convert

``` bash
pandoc -t revealjs -s -o myslides.html myslides.md -V revealjs-url=https://unpkg.com/reveal.js@3.9.2/
```

## Render Markdown at the command line

[Glow](https://github.com/charmbracelet/glow) is a terminal markdown renderer written in go.  There iis a prebuilt binary that can simply be unzipped and executed to render markdow.

``` bash
wget https://github.com/charmbracelet/glow/releases/download/v0.2.0/glow_0.2.0_linux_x86_64.tar.gz
tar -xzf glow_0.2.0_linux_x86_64.tar.gz
chmod +x glow
sudo mv glow /usr/bin

glow <filename>
```

## Autocomplete for click applications

see the [docs](https://click.palletsprojects.com/en/7.x/bashcomplete/) for more details

## Autocomplete for non click python cli's

shtab [https://github.com/iterative/shtab](https://github.com/iterative/shtab "https://github.com/iterative/shtab")

## Ensure functions reset context


``` bash
project_log() {
   _dir=$(pwd)
   _project_log() {
      cd ~/projects/project
      git log
   }
   _project_log $@ && cd $_dir || cd $_dir
}
```
