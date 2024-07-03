---
date: 2024-04-05 20:43:32
templateKey: til
title: fastapi jinja url_for with query params
published: true
jinja: false
tags:
  - python

---

Out of the box Starlette does not support url_for with query params.  When
trying to use url_for with query params it throws the following error.

``` python
starlette.routing.NoMatchFound: No route exists for name "infinite" and params "page"
```

In my searching for this I found [starlette issue #560](https://github.com/encode/starlette/issues/560) quite helpful, but not complete, as it did not work for me.

``` python
import jinja2

if hasattr(jinja2, "pass_context"):
    pass_context = jinja2.pass_context
else:
    pass_context = jinja2.contextfunction

@pass_context
def url_for_query(context: dict, name: str, **params: dict) -> str:
    request = context["request"]
    url = str(request.url_for(name))
    if params == {}:
        return url
    from urllib.parse import parse_qs, urlencode, urlparse, urlunparse

    # Parse the URL
    parsed_url = urlparse(url)

    # Parse the query parameters
    query_params = parse_qs(parsed_url.query)

    # Update the query parameters with the new ones
    query_params.update(params)

    # Rebuild the query string
    updated_query_string = urlencode(query_params, doseq=True)

    # Rebuild the URL with the updated query string
    updated_url = urlunparse(
        (
            parsed_url.scheme,
            parsed_url.netloc,
            parsed_url.path,
            parsed_url.params,
            updated_query_string,
            parsed_url.fragment,
        )
    )

    if os.environ.get("ENV") in ["dev", "qa", "prod"]:
        updated_url = updated_url.replace("http", "https", 1)

    return updated_url

def get_templates():
    templates = Jinja2Templates(directory="templates")
    templates.env.globals["url_for"] = url_for_query
    return templates
```

!!! Note "https"
    If you want url_for to work in production you need some way to convert http
    to https.  Here is how I make it work, for local development I `export
    ENV=local` then for each environment that I am running on a server I include
    it in the list and update `ENV` appropriately.

    ``` python
        if os.environ.get("ENV") in ["dev", "qa", "prod"]:
            updated_url = updated_url.replace("http", "https", 1)
    ```

The route might look something like this.

``` python
@infinite_router.get("/")
async def home(request: Request, page: int = 1, n: int = 10):
  ...
```

To access the home route using url_for in a jinja template you can use the
following, once you have applied the `url_for_query` function as your default
`url_for`

``` html
<a href="{{ url_for('home', page=1) }}">Home</a>
```
