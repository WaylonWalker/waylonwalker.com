---
date: 2024-04-05 20:43:32
templateKey: til
title: fastapi jinja url_for with query params
published: true
tags:
  - python

---

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

    return updated_url
```
