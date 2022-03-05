---
date: 2022-03-05 16:23:42.121622
templateKey: til
title: Grouping Mermaid nodes in Subgraphs
tags:
  - webdev

---

Mermaid provides some really great ways to group or fence in parts of your
graphs through the use of subgraphs.

Here we can model some sort of data ingest with some raw iot device and our
warehouse in different groups.

```
graph TD;

    subgraph raw_iot
        a
    end

    subgraph warehouse
        A --> B
        B --> C
    end
```
<script src='https://unpkg.com/mermaid@8.1.0/dist/mermaid.min.js'></script>
<div class='mermaid'>
graph TD;

    subgraph raw_iot
        a
    end

    subgraph warehouse
        A --> B
        B --> C
    end
</div>

## connecting subgroups

If we want to connect them, we can make a connection between a and A outside of
the subgraphs.

```
graph TD;

    subgraph raw_iot
        a
    end

    a --> A

    subgraph warehouse
        A --> B
        B --> C
    end
```
<script src='https://unpkg.com/mermaid@8.1.0/dist/mermaid.min.js'></script>
<div class='mermaid'>
graph TD;

    subgraph raw_iot
        a
    end

    a --> A

    subgraph warehouse
        A --> B
        B --> C
    end
</div>

## separation of concerns

It's also possible to specify subgraphs separate from where you define your
nodes. which allows for some different levels of grouping that would not be
possible if you were to define all your nodes inside of a subgraph.

```
graph TD;
    a --> A
    A --> B
    B --> C

    subgraph one
        A
        C
    end
```


<div class='mermaid'>
graph TD;
    a --> A
    A --> B
    B --> C

    subgraph raw_iot
        a
    subgraph warehouse
        A
        C
    end
</div>
