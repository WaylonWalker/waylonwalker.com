---
date: 2022-01-18 20:13:32.860641
templateKey: til
title: Get Python docstring with ast
tags:
  - python

---

Getting docstrings from python's ast is far simpler and more reliable than any
method of regex or brute force searching.  It's also much less intimidating
than I originally thought.

## Parsing

First you need to load in some python code as a string, and parse it with
`ast.parse`.  This gives you a tree like object, like an html dom.

``` python
py_file = Path("plugins/auto_publish.py")
raw_tree = py_file.read_text()
tree = ast.parse(raw_tree)
```

## Getting the Docstring

You can then use `ast.get_docstring` to get the docstring of the node you are
currently looking at.  In the case of freshly loading in a file, this will be
the module level doctring that is at the very top of a file.

``` python
module_docstring = ast.get_docstring(tree)
```

## Walking for all functions

To get all of the functions docstrings we can use `ast.walk` to look for nodes
that are an instance of `ast.FunctionDef`, then run `get_docstring` on those
nodes.

```python
functions = [f for f in ast.walk(tree) if isinstance(f, ast.FunctionDef)]
function_docs = [ast.get_docstring(f) for f in functions]
```

> ast.walk docs: Recursively yield all descendant nodes in the tree starting at *node*
(including *node* itself), in no specified order.  This is useful if you
only want to modify nodes in place and don't care about the context.

## Example

Here is an image of me running this example through `ipython`.

![getting docstrings from the ast in python](https://images.waylonwalker.com/ast-get-docstring.png)
