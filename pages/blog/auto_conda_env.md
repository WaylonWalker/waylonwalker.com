---
templateKey: blog-post
tags: ['python', ]
title: Automatic Conda Environments
date: 2021-03-22T00:00:00 
status: draft

---


I've really been digging my new tmux session management setup.  Now I have
leveled it up by adding direnv to my workflow.  It will execute a shell script
whenever I cd into a directory.  One thing I wanted to add to this was,
automatic activation of python environments whenever I cd into a directory, or
create a new environment if one does not exist.

## Final Result

### Venv
``` bash
#!/bin/bash
# shortcut for creating new conda environments based on the current working directory
condanew() {
    conda create -n $(basename $PWD) python=3.8 -y
    source activate $(basename $PWD)
}
echo $(basename $PWD) | lolcat
source activate $(basename $PWD) || condanew
```

### Conda
``` bash
#!/bin/bash
# shortcut for creating new conda environments based on the current working directory
condanew() {
    conda create -n $(basename $PWD) python=3.8 -y
    source activate $(basename $PWD)
    pip install lolcat
}
echo $(basename $PWD) | lolcat
source activate $(basename $PWD) || condanew
```
