---
date: 2022-02-01 16:17:18.632158
templateKey: til
title: Find all Headings with BeautifulSoup
tags:
  - python
  - webdev

---

BeautifulSoup is a DOM like library for python.  It's quite useful to
manipulate html.  Here is an example to find_all html headings.  I stole
the regex from stack overflow, but who doesn't.

## Make an example
_sample.html_

Lets make a sample.html file with the following contents.  It mainly has
some headings, `<h1>` and `<h2>` tags that I want to be able to find.

```html
<!DOCTYPE html>
<html lang="en">
  <body>
    <h1>hello</h1>
    <p>this is a paragraph</p>
    <h2>second heading</h2>
    <p>this is also a paragraph</p>
    <h2>third heading</h2>
    <p>this is the last paragraph</p>

  </body>
</html>
```

## Get the headings with BeautifulSoup

Lets import our packages, read in our `sample.html` using pathlib and find all
headings using BeautifulSoup.

```python
from bs4 import BeautifulSoup
from pathlib import Path

soup = BeautifulSoup(Path('sample.html').read_text(), features="lxml")
headings = soup.find_all(re.compile("^h[1-6]$"))
```

And what we get is a list of `bs4.element.Tag`'s.

```python
>> print(headings)
[<h1>hello</h1>, <h2>second heading</h2>, <h2>third heading</h2>]
```

I recently added a heading_link plugin to markata, you might notice the
🔗's next to each heading on this page, that is powered by this exact
technique.
