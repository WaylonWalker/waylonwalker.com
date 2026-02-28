---
title: '💭 </> htmx ~ Locality of Behaviour (LoB)'
date: 2023-10-28T01:11:56
template: link
link: https://htmx.org/essays/locality-of-behaviour/
tags:
  - htmx
  - webdev
  - thoughts
  - thought
  - link
published: true

---

![[https://htmx.org/essays/locality-of-behaviour/]]

Interesting principle here.  What a great example, If I'm looking at the second jQuery example, I have to dig into dev tools or make some assumtions that this team uses jQuery, and selects by id, therefore I can grep for `$("#d1")`.

> Consider two different implementations of an AJAX request in HTML, the first in htmx:
``` heml
<button hx-get="/clicked">Click Me</button>


> and the second in jQuery:

``` js
  $("#d1").on("click", function(){
    $.ajax({
         /* AJAX options... */
    });
  });
```
``` html
<button id="d1">Click Me</button>
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
