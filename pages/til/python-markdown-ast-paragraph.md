---
date: 2022-02-05 02:18:28.911225
templateKey: til
title: Using a Python Markdown ast to Find All Paragraphs
tags:
  - python
  - webdev

---

In looking for a way to automatically generate descriptions for pages I
stumbled into a markdown ast in python.  It allows me to go over the
markdown page and get only paragraph text.  This will ignore headings,
blockquotes, and code fences.


``` python
import commonmark
import frontmatter

post = frontmatter.load("post.md")
parser = commonmark.Parser()
ast = parser.parse(post.content)

paragraphs = ''
for node in ast.walker():
    if node[0].t == "paragraph":
        paragraphs += " "
        paragraphs += node[0].first_child.literal
```

It's also super fast, previously I was rendering to html and using
beautifulsoup to get only the paragraphs.  Using the commonmark ast was
about 5x faster on my site.

### Duplicate Paragraphs

When I originally wrote this post, I did not realize at the time that
commonmark duplicates nodes.  I still do not understand why, but I have had
success duplicating them based on the source position of the node with the
snippet below.

``` python
from itertools import compress

import commonmark
import frontmatter

post = frontmatter.load("post.md")
parser = commonmark.Parser()
ast = parser.parse(post.content)

# find all paragraph nodes
paragraph_nodes = [
    n[0]
    for n in ast.walker()
    if n[0].t == "paragraph" and n[0].first_child.literal is not None
]
# for reasons unknown to me commonmark duplicates nodes, dedupe based on sourcepos
sourcepos = [p.sourcepos for p in paragraph_nodes]
# find first occurence of node based on source position
unique_mask = [sourcepos.index(s) == i for i, s in enumerate(sourcepos)]
# deduplicate paragraph_nodes based on unique source position
unique_paragraph_nodes = list(compress(paragraph_nodes, unique_mask))
paragraphs = " ".join([p.first_child.literal for p in unique_paragraph_nodes])
```
