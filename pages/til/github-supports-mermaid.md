---
date: 2022-02-24 15:22:31.386290
templateKey: til
title: GitHub Markdown now Supports Mermaid Diagrams
tags:
  - python

---

Mermaid diagrams provide a way to display graphs defined as plain text.
Some markdown renderers support this as a plugin.  GitHub now supports
it.

## example

You can define nodes like this in mermaid, and GitHub will now render
them as a pretty graph diagram.  Its rendered in svg, so its searchable
with `control f` and everything.

```mermaid
  graph TD;
      A-->B;
      A-->C;
      B-->D;
      C-->D-->OUT;
      E-->F-->G-->OUT
```

![Here is what the example looks like on
GitHub](https://images.waylonwalker.com/example-gh-mermaid.png)

## Links

* [GitHub support announcement](https://github.blog/2022-02-14-include-diagrams-markdown-files-mermaid/)
* [mermaid docs](https://mermaid-js.github.io/mermaid/#/)
