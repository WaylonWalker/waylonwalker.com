---
date: 2022-10-17 14:28:33
templateKey: til
title: running aws cli commands with localstack
published: false
tags:
  - aws

---

Upon first running an `aws` cli command using localstack you might end up with the following error.

``` bash
Unable to locate credentials. You can configure credentials by running "aws configure".
```

## Easy way

The easy easiest way is to leverage a package called `awscli-local`.

``` bash
pipx install awscli-local
```

## Leveraging the awscli

If you want to use the cli pro


``` bash
pipx install awscli

aws config --profile localstack
# put what you want for the keys, but enter a valid region like us-east-1

alias aws='aws --endpoint-url http://localhost:4566 --profile localstack'
```
