---
date: 2022-10-17 08:55:26
templateKey: til
title: localstack status permission
status: 'published'
tags:
  - aws

---

I ran into an issue where I was unable to ask localstack for its status. I
would run the command and it would tell me that it didn't have permission to
read files from my own home directory.  Let's fix it

## The issue

I would run this to ask for the status.

``` bash
localstack status
```

And get this error

``` bash
PermissionError: [Errno 13] Permission denied: '/home/waylon/.cache/localstack/image_metadata'
```

## What happened

It dawned on me that the first time I ran localstack was straight docker, not
the python cli.  When docker runs it typically runs as root unless the
Dockerfile sets up a user and group for it.

## How to fix it

If you have sudo access to the machine you are on you can recursively change
ownership to your user and group.  I chose to just give myself ownership of my
whole `~/.cache directory` you could choose a deeper directory if you want.  I
feel pretty safe giving myself ownership to my own cache directory on my own
machine.

``` bash
whoami
# waylon

chown -R waylon:waylon ~/.cache
```
