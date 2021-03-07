---
templateKey: blog-post
tags: ['python', 'bash']
title: Ipython Ninjitsu
date: 2020-12-14T00:00:00
status: draft
description: ''
cover: "/static/ipython-ninjitsu.png"

---


* ?docstring
* ??sourcecode
* %run
* %debug
* %autoreload
* %history
* autoformat
* %reset
* !shell commands

## ?docstring

Stop going to google everytime your stuck and stay in your workflow.  The
ipython `?` is a superhero for productivity and staying on task.

``` python
from kedro.pipeline import Pipeline
Pipeline?

Init signature:
Pipeline(
    nodes: Iterable[Union[kedro.pipeline.node.Node, ForwardRef('Pipeline')]],
    *,
    tags: Union[str, Iterable[str]] = None,
)
Docstring:
A ``Pipeline`` defined as a collection of ``Node`` objects. This class
treats nodes as part of a graph representation and provides inputs,
outputs and execution order.
Init docstring:
Initialise ``Pipeline`` with a list of ``Node`` instances.

Args:
    nodes: The iterable of nodes the ``Pipeline`` will be made of. If you
        provide pipelines among the list of nodes, those pipelines will
        be expanded and all their nodes will become part of this
        new pipeline.
    tags: Optional set of tags to be applied to all the pipeline nodes.

Raises:
    ValueError:
        When an empty list of nodes is provided, or when not all
        nodes have unique names.
    CircularDependencyError:
        When visiting all the nodes is not
        possible due to the existence of a circular dependency.
:
```

**Note** This does jump you into a pager, a j,k or up, down to navigate, q to quit.


## ??sourcecode

Docstring not enough for you use case.  I often run into cases where the
docstring is not clear enough and I need to see the implementation for myself
to see what a function does.

## %run

I turned my nose up at this one, prior to seeing the famous [I don't like
notebooks](https://www.youtube.com/watch?v=7jiPeIFXb6U) by 
[Joel Grus](https://joelgrus.com/).  My first snobby reaction was that
developing modules and using autoreload was superior.  I have since realized
there is a place for `%run`, and it can cut down on some keystrokes to import,
setup, and run even when developing in modules.

## %debug

ipython comes with a post-mortem debugger, and it can be a lifesaver.  If we
have a long running function that runs into an error it can be a complete buzzkill.

``` python
def long_func():
   import time
   time.sleep(12)
   n = 12
   df = pd.Data({'a': range(n)})
   return df

long_func()
```

## %reset

https://waylonwalker.com/reset-ipython

## %autoreload

https://waylonwalker.com/autoreload-ipython

``` python
c.InteractiveShellApp.extensions = ["autoreload"]
c.InteractiveShellApp.exec_lines = ["%autoreload 2"]
c.InteractiveShellApp.exec_lines.append(
    'print("Warning: disable autoreload in ipython_config.py to improve performance.")'
)
```

> place this in your ~/.ipython/profile_default/ipython_config.py to auto reload without needing to run the magic every time

## autoformat

This is a relatively new feature to ipython.  I really enjoy it, as the time
that I need the most help autoformatting my code is riffing on an ad hoc
analysis at the command line.

``` python
c.TerminalInteractiveShell.autoformatter = "black"
```

> place this in your ~/.ipython/profile_default/ipython_config.py to autoformat with black by default

## new prompt

## reverse history search

_Control R_

