---
date: 2024-11-18 15:29:30
templateKey: til
title: price an stl print on slant3d
published: true
tags:
  - python

---

I've been playing with 3d printing some items through the slant3d api.  I've
been pricing out different prints by running a slice request through their api.

## make a project

I've been using uv for project management. It's been working well for quick
projects like this while making it reproducible, I'm still all in on hatch for
libraries.

``` bash
mkdir slantproject
cd slantproject
uv init
uv venv
. ./.venv/bin/activate
uv add httpx rich python-dotenv
```

## Get an api key

You will need an api key from the slant api, which currently requires a google
account and a credit card to create.

``` env
# .env
#  replace with your api key from https://api-fe-two.vercel.app/
SLANT_API_KEY=sl-**
```

## slicing an stl with teh slant api

Then you can run the python script to price out your print.  I'm not exactly
sure how this compares to an order, especially when you add in different
materials.

``` python
from dotenv import load_dotenv
import httpx
import os

load_dotenv()

stl_url = ''
api_key = os.environ["SLANT_API_KEY"]

api = httpx.Client(base_url="https://www.slant3dapi.com/api/slicer")

res = httpx.post(
    "https://www.slant3dapi.com/api/slicer",
    json={"fileURL": stl_url},
    headers={"api-key": api_key, "Content-Type": "application/json"},
    timeout=60,
)


print(res.json())
```
