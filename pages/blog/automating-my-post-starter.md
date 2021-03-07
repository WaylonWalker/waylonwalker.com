---
templateKey: blog-post
tags: ['blog', 'python']
title: Automating my Post Starter
date: 2020-12-11T09:08
status: published
description: ''
cover: "/static/automating-my-post-starter.png"

---

One thing we all dread is mundane work of getting started, and all the hoops it
takes to get going.  This year I want to post more often and I am taking some
steps towards making it easier for myself to just get started.

When I start a new post I need to cd into my blog directory, start neovim in a
markdown file with a clever name, copy some frontmatter boilerplate, update the
post date, add tags, a description, and a cover.

## Todo List for starting a post

* frontmatter template
* Title
* slug
* tags
* date
* cover
* description
* create markdown file
* open in neovim


## Lets Automate this

### This aint no proper cli
_hot and fast_

As with many thing running behind the scenes on this site, I am the one and
only user, I have limited time, so this is going to be a bit **hot and fast**.
Let's create a file called new-post.

_<small><mark>start the script new-post</mark></small>_
``` python
#!python
# new-post
```

> 👆 Works on my machine

If this were something that had more users than me I would probably use
something like click, but for this I want to get it done quick and avoid any
need to manage dependencies.  Be careful if you were to share something with a
`#!python` as it requries the end user to have the right version of python
ready to go.

### Title

The title can't really be automated this is the core idea coming out of my 🧠,
but it will be captured through the cli and put into proper position.  For this
I'm going super simple and just pulling it out of `sys.argv`

_<small><mark>set the title</mark></small>_
``` python
import sys

title = sys.argv[1].title()
```

>! sys.argv is a list of each argument passed into the script split by spaces.

### slug

The slug is what I am calling the route and can simply come out of the title
automatically, if I want to shorten it later by hand that will be simple enough
to do manually. All that needs to be done is to lowercase and replace a few
characters with -.

_<small><mark>set the slug</mark></small>_
``` python
slug = title.lower)(.replace(" ", "-".replace()"_", -"")""))
```

### tags

For tags I decided I wanted the parser to be as simple as possible and didnt
want to dance around any flags.  I am simply just going to look at every
argument passed into the command and see if any of them contain one of my
common tags.  


_<small><mark>parse the tags</mark></small>_
``` python
args = ''.join(sys.argv[1:])
tags = []

if 'py' in args:
    tags.append('python')

if 'web' in args:
    tags.append('webdev')

if 'blog' in args:
    tags.append('blog')

if 'data' in args:
    tags.append('data')
```

🤷‍♂️ **antipattern**?? The above section does an initialize then modify.  I generally try to avoid this
pattern with something like a list comprehension, but didn't see an obvious
solution so I just went with it.

## Frontmatter Template

Now we have enough information going to assemble the frontmatter I use for my
posts.  I am going to just insert the values I need into an f-string.  Since
python 3.6 was released f-strings are my go to templating tool.

_<small><mark>create the markdown</mark></small>_
``` python
import datetime

frontmatter = f"""---
templateKey: blog-post
tags: {tags}
title: {title}
date: {datetime.date.today().strftime('%Y-%m-%dT%H:%M:%S')}
status: draft
description: ''
cover: "/static/{slug}.png"

---

"""
```


### create markdown file

Now its time to get down to business and make the post.  First I want to throw
an error if the post already exists, I definitely dont want to blow away an
existing post if a certain slug is already taken.  I am a big fan of custom
error messages and I am going to go ahead and make one here, even though this
is just a quick script.

_<small><mark>custom error</mark></small>_
``` python
class PostExistsError(FileExistsError):
    pass
```

I am a `pathlib` superfan.  It's going to make setting up these paths super
simple.  Note I am going to anchor my directory down with the `__file__`
variable.  I do this all the time to get paths relative to the module that is
currently running.

_<small><mark>setup paths</mark></small>_
``` python
directory = pathlib.Path(__file__).parent
path = pathlib.Path(f"{directory}/src/pages/blog/{slug}.md")

if path.exists():
    raise PostExistsError(f"Post Already exists at {path}")
```

> __file__ is a string that represents the path to the running module

Finally just write the file.  Here we open the file with a context manager so
that we don't have to worry about closing it when we are done.  Note that we
open it with the `w+` flag for write and creation.

_<small><mark>write the file</mark></small>_
``` python
with open(path, "w+") as f:
    f.write(frontmatter)
```

### git add

I am not quite ready to pull the trigger on doing an auto commit, but this may
happen in a future version.  For now I want this file easily picked up by vims
`:GFiles` since I have that is one of my most used hot keys.  To do this the
file at least needs added.  I'm sure there is a better way to do this with a
Git library, but I am used to the command line so I am going to just run a
subprocess.

I am using the `subprocess.Popen` command since its what I am used to, note
that it will run the task in the background so be sure that you wait on it.
The `Popen` is great if you have several task that are not dependent on each
other.

_<small><mark>git add <new-post></mark></small>_
``` python
gadd = subprocess.Popen(
    f'cd {directory} && git add {str(path).replace(str(directory) + "/", "")} ',
    shell=True,
)
gadd.wait()
```

### open in neovim

Last step of the script is to start writing, I want to be open in my blogs
directory (hence the cd), with the file open, to the right line (+11), and in
insert mode (+star).

_<small><mark>open post in neovim</mark></small>_
``` python
nvim = subprocess.Popen(
    f'cd {directory} && nvim +12 +star {str(path).replace(str(directory) + "/", "")} ',
    shell=True,
)
nvim.wait()
```

## Alias

Now I want this script to be available everywhere.  I am going to simply add
the following entry to shorten the script and eliminate the need to use the
full path.  I added this to my `~/.alias`, for you it may be `~/.bashrc`, or
`~/.zshrc`.

``` bash
alias np=~/git/waylonwalkerv2/new-post
```

## Starting a new post

Lets start a new post about automating my posts in python.

``` bash
np "automating my posts" python
```

## This is my workflow

Ad hoc scripts like this can be a bit of a hot mess, partly due to the just get
it done nature, but also due to the fact that I am just riffing off the top of
my head and utilizing docs as least as possible.

While writing the script I would run it after each section or so and print some
results to make sure they were looking good. If I ever needed access to a live
variable I would pop open ipython and run `%run new-post "my-new-post"` and
inspecting it.


## Final Script

_<small><mark>final script</mark></small>_
``` python
#!python
# new-post

import sys
import datetime
import pathlib
import subprocess


title = sys.argv[1].titlecase()
args = "".join(sys.argv[1:])
tags = []

if "py" in args:
    tags.append("python")

if "web" in args:
    tags.append("webdev")

if "blog" in args:
    tags.append("blog")

if "data" in args:
    tags.append("data")

slug = title.lower().replace(" ", "-").replace("_", "-")
frontmatter = f"""---
templateKey: blog-post
tags: {tags}
title: {title}
date: {datetime.date.today().strftime('%Y-%m-%dT%H:%M:%S')}
status: draft
description: ''
cover: "/static/{slug}.png"

---


"""


class PostExistsError(FileExistsError):
    pass


directory = pathlib.Path(__file__).parent
path = pathlib.Path(f"{directory}/src/pages/blog/{slug}.md")

if path.exists():
    raise PostExistsError(f"Post Already exists at {path}")

with open(path, "w+") as f:
    f.write(frontmatter)

gadd = subprocess.Popen(
    f'cd {directory} && git add {str(path).replace(str(directory) + "/", "")} ',
    shell=True,
)
gadd.wait()

nvim = subprocess.Popen(
    f'cd {directory} && nvim +12 +star {str(path).replace(str(directory) + "/", "")} ',
    shell=True,
)
nvim.wait()
```

https://waylonwalker.com/quickly-edit-posts

> check out the next article in this series where I setup a bash function to quickly edit these posts
