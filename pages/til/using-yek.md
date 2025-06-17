---
date: 2025-06-11 11:01:34
templateKey: til
title: using yek to serialize text files into llm friendly file
published: true
tags:
  - llm

---

I've been using gitingest [[ thoughts-516 ]] for quite awhile to serialize git repo into llm
friendly text files.  This gives tools context about repos that are not in the
training data so that it knows about it and how to use the code in the repo.

I had a use case for a project not yet on git, and found yek.

## Installing yek

Their instructions tell you to curl to bash.

``` bash
curl -fsSL https://bodo.run/yek.sh | bash
```

I don't like curl to bash from random sites, so I have my own self hosted
version of i.jpillora.com.  I like using this because it pulls from github and
I trust github as a source for artifacts as good as the repo I am pulling
from.

``` bash
curl https://i.jpillora.com/bodo-run/yek | bash
```

## Using yek

``` bash
yek
```

> /tmp/yek-output/yek-output-bb01e621.txt

This will give you a link to a text file that you can add to many llm tools.
This happened so fast for me that I didn't even believe that it worked
properly.

## more options

As with most clis, you can run `yek --help` to see the options available.

``` bash
yek --help
```
