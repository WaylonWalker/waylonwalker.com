---
date: 2022-03-14 18:30:12.830224
templateKey: til
title: Install yq | A light weight yaml parser cli
tags:
  - linux
  - cli
jinja: false

---

`yq` is a command line utility for parsing and querying yaml, like `jq` does for json.

## This is for me

I love that all of these modern tools built in go and rust, just give you a
zipped up executable right from GitHub releases, but it's not necessarily
straight forward how to install them.  `yq` does one of the best jobs I have
seen, giving you instructions on how to get a specific version and install it.


I use a bunch of these tools, and for what its worth I trust the devs behind
them to make sure they don't break.  This so far has worked out well for me,
but if it ever doesn't I can always pick an older version.

## Just give me the latest

Since I am all trusting of them I just want the latest version.  I do not want
to update a shell script with new versions, or even care about what then next
version is, I just want it. Luckily you can script the release page for the
latest version on all that I have came accross.

## What is the latest

I wrote or stole, I think I wrote it, this line of bash quite awhile ago, and
it has served me well for finding the latest release for any GitHub project
using releases.  Just update it with the name of the tool, org, and repo and it
works.

``` bash
YQ_VERSION=$(curl --silent https://github.com/mikefarah/yq/releases/latest | tr -d '"' | sed 's/^.*tag\///g' | sed 's/>.*$//g' | sed 's/^v//')
```

## Install with your shell

Now that we know how to consistently get the right version, I generally right
click the release in the releases page, replace the version with
`${TOOL_VERSION}` and put it in this wget call, then move the binary over to `~/.local/bin`

``` bash
local tmp=`mktemp -dt install-XXXXXX`
pushd $tmp
YQ_VERSION=$(curl --silent https://github.com/mikefarah/yq/releases/latest | tr -d '"' | sed 's/^.*tag\///g' | sed 's/>.*$//g' | sed 's/^v//')
wget https://github.com/mikefarah/yq/releases/download/v${YQ_VERSION}/yq_linux_amd64.tar.gz -O- -q | tar -zxf - -C /tmp
cp yq_linux_amd64 ~/.local/bin/yq
popd
```

## Install with ansible

Now I don't want to worry about missing `yq` again, so I am added it to my
ansible install script.  This way it's installed everyt time I setup a new
system with all of my favorite cli's.

``` yaml
- name: check is yq installed
  shell: command -v yq
  register: yq_exists
  ignore_errors: yes
  tags:
    - yq

- name: Install yq
  when: yq_exists is failed
  shell: |
    local tmp=`mktemp -dt install-XXXXXX`
    pushd $tmp
    YQ_VERSION=$(curl --silent https://github.com/mikefarah/yq/releases/latest | tr -d '"' | sed 's/^.*tag\///g' | sed 's/>.*$//g' | sed 's/^v//')
    wget https://github.com/mikefarah/yq/releases/download/v${YQ_VERSION}/yq_linux_amd64.tar.gz -O- -q | tar -zxf - -C /tmp
    cp yq_linux_amd64 {{ lookup('env', 'HOME') }}/.local/bin/yq
    popd
  tags:
    - yq
```

## Links

This is how I installed it, of course you can always follow Mike's instructions
from the repo.

* [yq repo](https://github.com/mikefarah/yq)
* [yq docs](https://mikefarah.gitbook.io/yq/)
