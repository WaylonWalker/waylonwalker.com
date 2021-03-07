---
templateKey: blog-post
related_post_label: Check out this related post
tags: []
title: What is something that you recently learned that you wish you would have learned
  or understood earlier?
date: 2020-01-10T06:00:00Z
status: published
description: What is something that you recently learned that you wish you would have
  learned or understood earlier?
cover: "/static/david-travis-aVvZJC0ynBQ-unsplash.jpg"

---
Cover Photo I call **gaining clarity** by [David Travis](https://unsplash.com/@dtravisphd?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/clarity?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

***

Mine is the python debugger. I was a long holdout thinking that print statements were sufficient. That was untill I started having errors crop up in functions that took minutes to run. The thing that I most notably wish I would have known about is post_mortem.

# Example

    [ins] In [4]: def repeater(msg, repeats=1):
             ...:     "repeats messages {repeats} number of times"
             ...:     print(f'{msg}\n' * repeats)

    [ins] In [5]: repeater('hi', 3)
    hi
    hi
    hi

    [ins] In [6]: repeater('hi', 'a')
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-6-0ec595774c81> in <module>
    ----> 1 repeater('hi', 'a')

    <ipython-input-4-530890de75cd> in repeater(msg, repeats)
          1 def repeater(msg, repeats=1):
          2     "repeats messages {repeats} number of times"
    ----> 3     print(f'{msg}\n' * repeats)
          4

# Debug with iPython/Jupyter

    %debug

# Vanilla Debug

    import pdb
    import sys

    pdb.post_mortem(sys.last_traceback)

# More

For more information about the debugger checkout the real python article. [https://realpython.com/python-debugging-pdb/](https://realpython.com/python-debugging-pdb/ "https://realpython.com/python-debugging-pdb/")

Also keep a bookmark of the table of pdb commands from the article [https://realpython.com/python-debugging-pdb/#essential-pdb-commands](https://realpython.com/python-debugging-pdb/#essential-pdb-commands "https://realpython.com/python-debugging-pdb/#essential-pdb-commands")

# Debug Session

[![debug session](https://res.cloudinary.com/practicaldev/image/fetch/s--ShQ3NN06--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/1tnri6wdwimwk7i83cvg.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--ShQ3NN06--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/1tnri6wdwimwk7i83cvg.png)
