---
date: 2022-03-02 14:52:08.564231
templateKey: til
title: Bash mktemp
tags:
  - bash
  - cli
  - linux

---
There is GNU coreutils command called `mktemp` that is super handy in shell
scripts to make temporary landing spots for files so that they never clash with
another instance, and will automatically get cleaned up when you restart, or
whenever `/tmp` gets wiped.  I'm not sure when that is, but I don't expect it
to be long.

## Making temp directories

Here are some examples of making temp directories in different places, my
favorite is `mktemp -dt mytemp-XXXXXX`.

``` bash
# makes a temporary directory in /tmp/ with the defaul template tmp.XXXXXXXXXX
mktemp

# makes a temporary directory in your current directory
mktemp --directory mytemp-XXXXXX
# shorter version
mktemp -d mytemp-XXXXXX

# same thing, but makes a file
mktemp mytemp-XXXXXX

# makes a temporary directory in your /tmp/ directory (or what ever you have configured as your TMPDIR)
mktemp --directory --tmpdir mytemp-XXXXXX
# shorter version
mktemp -dt mytemp-XXXXXX

# same thing, but makes a file
mktemp --tmpdir mytemp-XXXXXX
# shorter version
mktemp -t mytemp-XXXXXX
```

## Use Case

Here is a sample script that shows how to capture the tempdir as a variable and
reuse it.  Here is an example of curling my bootstrap file into a temp
directory and running it from that directory.

``` bash
local tmp=`mktemp -dt bootstrap-XXXXXX`
pushd $tmp
curl https://raw.githubusercontent.com/WaylonWalker/devtainer/main/bootstrap > bootstrap
bash bootstrap
popd
```

## Templates

You must have at least 3 trailing X's that mktemp will replace with random
characters.  I played with it for a bit, it kinda allows for some trailing
characters, and will not fill groups of X's earlier in your template, only the
last consecutive string.

My randomm samples I played with.

``` bash
waylonwalker.com on  main [!?]  v3.9.7 (waylonwalker.com) took 2m24s
❯ mktemp myXtemp-XaXbXXXX -dt
/tmp/myXtemp-XaXbx9hn

waylonwalker.com on  main [!?]  v3.9.7 (waylonwalker.com)
❯ mktemp myXtemp-XaXbXXXXs -dt
/tmp/myXtemp-XaXb2tpGs

waylonwalker.com on  main [!?]  v3.9.7 (waylonwalker.com)
❯ mktemp myXtemp-XaXbXXcXXs -dt
mktemp: too few X's in template ‘myXtemp-XaXbXXcXXs’

waylonwalker.com on  main [!?]  v3.9.7 (waylonwalker.com)
❯ mktemp myXtemp-XaXbXXcXXs -dt

waylonwalker.com on  main [!?]  v3.9.7 (waylonwalker.com)
❯ mktemp myXtemp-XaXbXXXXt -dt
/tmp/myXtemp-XaXbe8PWt

waylonwalker.com on  main [!?]  v3.9.7 (waylonwalker.com)
❯ mktemp myXtemp-XXX-you-XXX -dt
/tmp/myXtemp-XXX-you-48l

waylonwalker.com on  main [!?]  v3.9.7 (waylonwalker.com)
❯ mktemp myXtemp-XXX-you-XX -dt
mktemp: too few X's in template ‘myXtemp-XXX-you-XX’
```

## RTFM

The man page has good stuff on all the flags that you might need.
``` bash
man mktemp
```
