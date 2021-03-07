---
templateKey: blog-post
related_post_label: Check out this related post
tags: []
title: Interrogate is a pretty awesome, brand new, cli for Python packages
date: 2020-05-15T03:00:00.000+00:00
status: published
description: dead simple docstring coverage for your python project
cover: "/static/interrogate-python.png"

---
As usual while listening to [python bytes 181](https://pythonbytes.fm/episodes/show/181/it-s-time-to-interrogate-your-python-code) I heard of a tool that I had to try out right away!

This thing is 🔥 hot off the press folks, we're talking the first release only 3 weeks ago. Its something that the python community needed years ago, and it belongs in your CI **today**. I had tried several tools that tried to do docstring coverage in the past but they were a bit cumbersome and were quickly forgotten about. Not interrogate, its dead simple!

> Nothing I have tried has come close to being this good

## Interrogate

It runs documentation coverage for your python project. It allows you to set the minimum amount of docstring coverage for your project and has some great setup instructions right in the readme.

## Install it

Interrogate is on pypi so it is super simple to install with `pip`

```
pip install interrogate
```

## run it

This is the best part, its super easy to run right from the command line! Just call it, and give it a path to run.

```
interrogate -v <path>
```

## 😲 I have some work to do

One of my new open source packages [find-kedro](https://find-kedro.waylonwalker.com/) only hit 71%.

```
interrogate find-kedro -v
```

![verbose interrogate on find-kedro](https://images.waylonwalker.com/interrogate-python-v.png)

Personally I really like the **double verbose** output that gives you the names of everything missing a docstring and the line they occur on.

```
interrogate find-kedro -vv
```

![double verbose interrogate on find-kedro](https://images.waylonwalker.com/interrogate-python-vv.png)

## Give it a ⭐
Every project this amazing deserves a big ol ⭐ on GitHub! Go over to [econchick/interrogate](https://github.com/econchick/interrogate) and give it a one... it deserves it! While you are there check out the **wicked** good readme. It has great examples of how to run it from your command line, as a pre-commit hook, in your ci, with your code, or pyproject.toml.

> While you are there check out the **wicked** good readme!
