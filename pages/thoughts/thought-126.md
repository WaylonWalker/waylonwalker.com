---
title: '💭 Automatic browser reloading in FastAPI'
date: 2023-10-08T15:16:56
templateKey: link
link: https://gist.github.com/vrslev/6d0602bfa939a01844f645c608afb85a
tags:
  - webdev
  - fastapi
published: true

---

> I just discovered [arel](https://pypi.org/project/arel/) for hot reloading python applications when content changes from this snippet that implements it for fatapi.

On app startup add the `/hot-reload` routes if in **DEBUG** mode.

``` python

import os

import arel
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates("templates")

if _debug := os.getenv("DEBUG"):
    hot_reload = arel.HotReload(paths=[arel.Path(".")])
    app.add_websocket_route("/hot-reload", route=hot_reload, name="hot-reload")
    app.add_event_handler("startup", hot_reload.startup)
    app.add_event_handler("shutdown", hot_reload.shutdown)
    templates.env.globals["DEBUG"] = _debug
    templates.env.globals["hot_reload"] = hot_reload


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", context={"request": request})

# run:
# DEBUG=true uvicorn main:app --reload
```

install `arel` and make sure you have `uvicorn[standard]` for websocket support.

``` text
fastapi
uvicorn[standard]
arel
jinja2
```

In the template, load the script when in debug mode.

``` html
<body>
  {% block content %}{% endblock %}

  <!-- Hot reload script -->
  {% if DEBUG %} {{ hot_reload.script(url_for('hot-reload')) | safe }} {% endif
  %}
</body>
```

[Original thought](https://gist.github.com/vrslev/6d0602bfa939a01844f645c608afb85a)
