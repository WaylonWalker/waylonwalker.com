---
templateKey: blog-post
related_post_label: Check out this related post
tags: []
title: What is YOUR Advice for New Data Scientists
date: 2020-02-26T12:55:00Z
status: published
description: What is YOUR Advice for New Data Scientists
cover: "/static/16.png"

---
* Learn the business
* Learn Git
* Your code does not need to be amazing
* Keep Learning

# Learn Git

You dont have to start out as a git wizard with the cleanest possible commit history.  At first dont let yourself get too wrapped up in it, the most important part is that you make commits.  You will find needs for more advanced stuff later.


``` bash
git add .
git commit -m "FEAT added new function to calculate revenue by product family"
git push
```

Get comfortable with this, then learn how to `branch`, `rebase`, `stash`, etc...


# Your code does not need to be amazing

Get the job done.  Keep it in small bite size pieces.  Make readable function definitions and variable names.  You will thank yourself for naming things well later.  Readability counts more than performance in most cases of data science.  If it gets the job done try not to over worry about things like performance.  A few extra seconds to clean a dataset or build a model is not worth hours of your time.  As you go you will have cases that performance is more critical and you will learn what to do from the start to avoid them.
