---
templateKey: blog-post
tags: [python]
title: Windowing Python Lists
date: 2020-12-10T10:44:19
status: published
description: ''
cover: "/static/more-itertools-windowed.png"

---

In python data science we often will reach for pandas a bit more than necessary. While pandas can save us so much there are times where there are alternatives that are much simpler.  The itertools` and `more-itertools` are full of cases of this.

This post is a walkthrough of me solving a problem with `more-itertools` rather than reaching for a for loop, or pandas.

I am working on a  one-line-link expander for my blog.  I ended up doing it, just by modifying the markdown with python.  I first split the post into lines with `content.split('\n')`, then look to see if the line appears to be just a link.  One more safety net that I wanted to add was to check if there was whitespace around the line, this could not simply be done in a list comprehension by itself.  I need just a bit of knowledge of the surrounding lines, enter `more-itertools`.


## simplified rendering function

I have a function that will check to see if the line should be expanded, then render the correct template.  Fist step is to check if the line contains no spaces and starts with `https`, if it
does render the template. 

The real expand_line function uses requests to pull some metadata about the post to insert into the card, more on that in another post.

``` python
def expand_line(line):
   """
   Check if line should be expanded then render a template
   """

   if ' ' in line and line.startswith('https'):
      return line

  return f"<a href='{line}' class='card'>"
```

## initial implementation

My first implementation was to load in the content as a single string and use a list comprehension to expand each line.

``` python
expanded_content = "\n".join(
    [expand_line(line) for line in content]
)
```

## The issue.

Sometimes I write my posts in vim without wordwrap on and just use `gq` to wrap them to the current `textwidth`.  If I have a link that happens to be really long it ends up on its own line.  I do not want one line links to expand if they are in the middle of a paragraph.

``` markdown
## sample paragraph

This is a paragraph that has a really long link
https://waylonwalker.com/not-a-real-link-just-a-silly-example-for-this-post
inside of it that ends up on its own line
```

> I need a bit of knowledge about the lines around the link.


## windowing

`more-itertools` comes with a windowing function that will slide over an iterable with a width of n.

``` python
>>> from more_itertools import windowed
>>> all_windows = windowed([1, 2, 3, 4, 5], 3)
>>> list(all_windows)
[(1, 2, 3), (2, 3, 4), (3, 4, 5)])]
```

> this example is copied from the [more-itertools docs](https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.windowed)

## sliding through my content

The one extra that we need is padding at the front and back of the list so that we ensure that every value ends up in the middle position at least once.


``` python
expanded_content = "\n".join(
    [expand_line(*line) for line in windowed(f'\n{content}\n', 3)]
)
```

**meta**: 👇  This is an example of a one-line-link card that we are trying to achieve.


<a class="onelinelink" href="https://waylonwalker.com/python-args-kwargs/">
<img style="float: right;" align='right' src="https://images.waylonwalker.com/python-args-kwargs-slides-dev_250x105.png" alt="article cover">
<div class="right">
    <h2>understanding python *args and **kwargs</h2>
    <p class="description">
    Python `*args` and `**kwargs` are super useful tools, that when used properly can make you code much simpler and easier to maintain.  Large manual conversions from a dataset to function arguments can be packed and unpacked into lists or dictionaries. Beware though, this power **can** lead to some really unreadable/unusable code if done wrong.
    </p>
    <p class="url">
    <span class="read-more">read more</span>  waylonwalker.com
    </p>
</div>
</a>


> Not sure what *line is, check out this article.


## update expand_line

Now that we are calling `expand_line` with all three lines.  We need to update the function signature and add a guarding clause to return early if before or after lines are not blank.

``` python
def expand_line(before, line, after):
   """
   Check if line should be expanded then render a template
   """
    if before != '' and after != '':
      return line


    if ' ' in line and line.startswith('https'):
      return line

    return f"<a href='{line}' class='card'>"
```


Hope you liked this walk-through of solving a problem I had with `more-itertools`, If you learned something be sure to share it.
