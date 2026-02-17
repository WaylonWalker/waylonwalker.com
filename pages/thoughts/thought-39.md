---
title: '💭 </> htmx ~ The client-side-templates Extension'
date: 2023-07-28T14:59:37
templateKey: link
link: https://htmx.org/extensions/client-side-templates/
tags:
  - htmx
  - webdev
published: true

---

> Using templates with htmx requires the client-side-templates extension, and the template engine to be loaded in a `<script>` tag.

example htmx using templates.

``` html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <script src="https://unpkg.com/htmx.org"></script>
  <script src="https://unpkg.com/htmx.org/dist/ext/client-side-templates.js"></script>
  <script src="https://unpkg.com/mustache@latest"></script>
</head>
<body>
  <div hx-ext="client-side-templates">
    <button hx-get="https://jsonplaceholder.typicode.com/todos/1"
            hx-swap="innerHTML"
            hx-target="#content"
            mustache-template="foo">
      Click Me
    </button>

    <p id="content">Start</p>

    <template id="foo">
      <p> {% raw %}{{userID}}{% endraw %} and {% raw %}{{id}}{% endraw %} and {% raw %}{{title}}{% endraw %} and {% raw %}{{completed}}{% endraw %}</p>
    </template>
  </div>
</body>
</html>
```

[Original thought](https://htmx.org/extensions/client-side-templates/)
