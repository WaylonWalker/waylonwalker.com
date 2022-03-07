---
date: 2022-03-07 17:22:04.948869
templateKey: til
title: Mermaid Highlight
tags:
  - webdev

---

Mermaid gives us a way to style nodes through the use of css, but rather than
using normal css selectors we need to use `style <nodeid>`.  This also applies
to subgraphs, and we can use the name of the subgraph in place of the nodeid.

``` ruby
graph TD;
    a --> A
    A --> B
    B --> C

    style A fill:#f9f,stroke:#333,stroke-width:4px
    style B fill:#f9f,stroke:#333,stroke-width:4px

    subgraph one
        a
    end

    style one fill:#BADA55
```

produces the following graph

<script src='https://unpkg.com/mermaid@8.1.0/dist/mermaid.min.js'></script>
<div class='mermaid'>
graph TD;
a --> A
A --> B
B --> C
style A fill:#f9f,stroke:#333,stroke-width:4px
style B fill:#f9f,stroke:#333,stroke-width:4px
subgraph one
  a
end

style one fill:#BADA55
</div>
