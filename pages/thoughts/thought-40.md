---
title: '💭 python 3.x - FastAPI redirection for trailing slash returns no...'
date: 2023-07-28T14:59:37
templateKey: link
link: https://stackoverflow.com/questions/63511413/fastapi-redirection-for-trailing-slash-returns-non-ssl-link
tags:
  - fastapi
  - webdev
published: true

---

> I am trying to use htmx on a new fastapi site for my thoughts, and have been hitting this error. 

``` js
Mixed Content: The page at 'https://front.mydomain.com/#/clients/1' was loaded over HTTPS, but requested an insecure resource 'http://back.mydomain/jobs/?_end=25&_order=DESC&_sort=id&_start=0&client_id=1'. This request has been blocked; the content must be served over HTTPS.
```

## What is happening

I have an htmx component that gets the current users name, but if they are not logged in the backend redirects to a login form.

``` html
        <div hx-get='/users/me' hx-trigger='load'>
            get me
        </div>
```

But for some reason when the front end gets this redirect, it tries to do it through http, and flags it as insecure.

## The solution

To solve this issue, the post directs to set the `--forwarded-allow-ips` to '*'

``` bash
uvicorn thoughts.api.app:app --port 5000 --reload --log-level info --host 0.0.0.0 --workers 1 --forwarded-allow-ips '*'
```

[Original thought](https://stackoverflow.com/questions/63511413/fastapi-redirection-for-trailing-slash-returns-non-ssl-link)
