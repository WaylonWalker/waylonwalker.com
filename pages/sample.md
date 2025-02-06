---
templateKey: blog-post
tags: []
title: Sample
date: 2021-01-25T00:00:00
published: false

---

``` python
import this

print("that")
```

# title

## subtitle

!!! note sample note

     this is a sameple

!!! danger be careful

     this is super dang.

     ## subtitle

!!! reminder

     this is a reminder

!!! caution

     this is a caution

!!! attention

     this is a attention

!!! hint

     this is a hint

!!! error

     this is a error

!!! important

     this is a important

!!! seealso

     this is a seealso

!!! tip

     this is a tip

!!! todo

     this is a todo

!!! warning

     this is a warning

!!! settings

     this is a settings

html without the markdown atrribute will not be parsed as markdown

!!! vsplit ""

    !!! vsplit ""
        ``` markdown
        <div>
        # markdown in html

        This is not markdown
        </div>
        ``` markdown

    !!! vsplit ""
        <div>
        # markdown in html

        This is not markdown
        </div>

If you give an html tag the `markdown="1"` attribute, the markdown will be
parsed and rendered as html inside of that tag.

!!! vsplit ""
    !!! vsplit ""
        ``` markdown
        <div markdown="1">

        # markdown in html

        This is a *Markdown* Paragraph.

        </div>
        ```

    !!! vsplit ""
        <div markdown="1">

        # markdown in html

        This is a *Markdown* Paragraph.

        </div>

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
flowchart TD
    A[Raw Water Intake] --> B[Screening]
    B --> C[Coagulation & Flocculation]
    C --> D[Sedimentation/Clarification]
    D --> E[Filtration]
    E --> F[Disinfection]
    F --> G[Storage/Distribution]
```

```mermaid
    xychart-beta
    title "Sales Revenue"
    x-axis [jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec]
    y-axis "Revenue (in $)" 4000 --> 11000
    bar [5000, 6000, 7500, 8200, 9500, 10500, 11000, 10200, 9200, 8500, 7000, 6000]
    line [5000, 6000, 7500, 8200, 9500, 10500, 11000, 10200, 9200, 8500, 7000, 6000]
```

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---

graph TD
  A[\Replenish Value Add stock/] --->C
  B(Order product with Value Add) --->C
  C{Frequent process?} --->|Yes|D
  C --->|No|F
  D{New template?} --->|Yes|E
  D --->|No|G
  E(Create work order template) --->G
  F(Create work order) --->H
  G(Copy template to work order) --->I
  H(Add materials to work order processes) --->J
  I(Adjust material quantities) --->J
  J(Monitor work orders) --->K
  K{Material quantities in stock?} --->|No|L
  K --->|Yes|M
  L(Procure materials) --->M
  M(Change status to In Progress) --->N
  N{External Vendor to perform step?} --->|Yes|O
  N --->|No|P
  O(Add vendor costs) --->Q
  P[\Perform work order step/] --->R
  Q([Ship materials to Vendor]) --->S --->X
  R{Additional processing required?} --->|Yes|N
  R--->|No|T
  S[\Perform work order step/] --->U
  T(Receive final stock) --->V
  U(Receive product from vendor) --->W
  V(Ship product on order) --->Y
  W{Partial quantity received?} --->|Yes|X
  W --->|No|Z
  X[Create work order backorder] ---> J
  Y(Change status to complete) --->AA
  Z(Pay vendor invoice) --->R
  AA([Finish])
```

gitgraph

```mermaid

gitGraph:
    commit "Ashish"
    branch newbranch
    checkout newbranch
    commit id:"1111"
    commit tag:"test"
    checkout main
    commit type: HIGHLIGHT
    commit
    merge newbranch
    commit
    branch b2
    commit
```

```mermaid

gitGraph:
    commit "new stuff"
    branch make-server-feature
    checkout make-server-feature
    commit "go"
    commit tag:"test"
    commit
    commit
    commit
    rebase
    checkout main
    commit type: HIGHLIGHT
    commit
    merge make-server-feature
    commit

```

```mermaid
mindmap
  #python
    uv
    pip
    ipython
      jupyter
      jupyterlab


```

```mermaid
stateDiagram-v2
    [*] --> Still
    Still --> [*]
    Still --> Moving
    Moving --> Still
    Moving --> Crash
    Crash --> [*]
```

The journey

```mermaid
journey
    title My working day
    section Go to work
      Make tea: 5: Me
      Go upstairs: 3: Me
      Do work: 1: Me, Cat
      Play with cat: 10: Me, Cat
    section Go home
      Go downstairs: 5: Me
      Sit down: 5: Me
```

```mermaid
---
config:
  layout: elk
  look: handDrawn
  theme: dark
---
timeline
    title History of Social Media Platform
    2002 : LinkedIn
    2004 : Facebook
         : Google
    2005 : Youtube
    2006 : Twitter
```

```mermaid
architecture-beta
    group api(cloud)[API]

    service db(database)[Database] in api
    service disk1(disk)[Storage] in api
    service disk2(disk)[Storage] in api
    service server(server)[Server] in api

    db:L -- R:server
    disk1:T -- B:server
    disk2:T -- B:db

```

```mermaid
architecture-beta
    group api(logos:aws-lambda)[API]

    service db(logos:aws-aurora)[Database] in api
    service disk1(logos:aws-glacier)[Storage] in api
    service disk2(logos:aws-s3)[Storage] in api
    service server(logos:aws-ec2)[Server] in api

    db:L -- R:server
    disk1:T -- B:server
    disk2:T -- B:db


```

<script src="https://cdn.jsdelivr.net/npm/vega@5"></script>

<script src="https://cdn.jsdelivr.net/npm/vega-lite@5"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6"></script>

```vega
{
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "data": {"url": "https://vega.github.io/editor/data/barley.json"},
  "mark": "bar",
  "encoding": {
    "x": {"aggregate": "sum", "field": "yield", "type": "quantitative"},
    "y": {"field": "variety", "type": "nominal"},
    "color": {"field": "site", "type": "nominal"}
  }
}
```
