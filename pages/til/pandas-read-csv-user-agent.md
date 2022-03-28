---
date: 2022-03-28 01:21:30.473713
templateKey: til
title: Set User Agent on pandas read_csv
tags:
  - python

---

I keep a small [cars.csv](https://waylonwalker.com/cars.csv) on my website for
quickly trying out different pandas operations.  It's very handy to keep around
to help what a method you are unfamiliar with does, or give a teammate an
example they can replicate.

## Hosts switched

I recently switched hosting from netlify over to cloudflare.  Well cloudflare
does some work to block certain requests that it does not think is a real user.
One of these checks is to ensure there is a real user agent on the request.

## Not my go to dataset 😭

This breaks my go to example dataset.

```python
pd.read_csv("https://waylonwalker.com/cars.csv")

# HTTPError: HTTP Error 403: Forbidden
```

## But requests works???

What's weird is, requests still works just fine!  Not sure why using urllib the
way pandas does breaks the request, but it does.

```python
requests.get("https://waylonwalker.com/cars.csv")

<Response [200]>
```

## Setting the User Agent in pandas.read_csv

_this fixed the issue for me!_

After a bit of googling I realize that this is a common thing, and that setting
the user-agent fixes it.  This is the point I remember seeing in the cloudflare
dashbard that they protect against a lot of different attacks, aparantly it
treats `pd.read_csv` as an attack on my cloudflare pages site.

```python
pd.read_csv("https://waylonwalker.com/cars.csv", storage_options = {'User-Agent': 'Mozilla/5.0'})

# success
```

## Now my data is back

Now this works again, but it feels like just a bit more effort than I want to
do by hand.  I might need to look into my cloudflare settings to see if I can
allow this dataset to be accessed by `pd.read_csv`.
