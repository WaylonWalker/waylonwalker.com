---
title: '💭 fastapi https url_for'
date: 2024-03-24T18:15:48
template: link
link: None
tags:
  - fastapi
  - webdev
  - thoughts
  - thought
  - link
published: true

---

![[None]]


jinja's `url_for` in fastapi does not account for https by default, there is
probably a better way, but this is a way that allows me to configure when I use
http vs https.

``` python
@pass_context
def https_url_for(context: dict, name: str, **path_params: Any) -> str:
    """
    always convert http to https
    """
    request = context["request"]
    http_url = request.url_for(name, **path_params)
    return str(http_url).replace("http", "https", 1)


def get_templates(config: BaseSettings) -> Jinja2Templates:
    templates = Jinja2Templates(directory="templates")
    templates.env.globals["https_url_for"] = https_url_for

    ## only use the default url_for for local development, for dev, qa, and prod use https
    if os.environ.get("ENV") in ["dev", "qa", "prod"]:
        templates.env.globals["url_for"] = https_url_for
        console.print("Using HTTPS")
    else:
        console.print("Using HTTP")

    return templates
```


!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
