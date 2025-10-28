---
date: 2025-10-26 10:16:41
templateKey: til
title: uv s3 sync with dotenv
published: true
tags:
  - python

---

I often want to run an s3 sync in an isolated environment, I don't want to set
any environment variables, I don't want anything secret in my history, and I
don't want to change my dotenv into something that exports variables, I just
want s3 sync to work.  `dotenv run` is the tool that I've been using for this,
and this uv one liner lets it run fully isolated from the project.


## one liner

``` bash
uv tool run --from 'python-dotenv[cli]' dotenv run -- uv tool run --from awscli aws s3 sync s3://bucket data
```


## multi-line

same thing formatted for readability

``` bash
uv tool run \
  --from 'python-dotenv[cli]' \
  dotenv run -- \
uv tool run \
  --from awscli \
  aws s3 sync s3://dropper data
```

There are probably 10 ways to skin this cat, but this is what I did, if you
have a better way let me know, I'll link you below.
