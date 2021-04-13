---
templateKey: blog-post
tags: ['python', ]
title: Automatic Conda Environments
date: 2021-03-22T00:00:00 
status: draft

---

## Final Result

``` bash
#!/bin/sh
# shortcut for creating new conda environments based on the current working directory
condanew() {
    conda create -n $(basename $PWD) python=3.8 -y
    source activate $(basename $PWD)
}
source activate $(basename $PWD) || condanew
```
