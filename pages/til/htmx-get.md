---
date: 2022-03-25 00:49:23.204595
templateKey: til
title: Ease into htmx with htmx-get
tags:
  - webdev
  - webdev
  - webdev

---

I recently attended
[python web conf 2022](https://2022.pythonwebconf.com/)
and after seeing some incredible presentations on it I am excited to
give [htmx](https://htmx.org/) a try.

## The base page

Start with some html boilerplate, pop in a script tag to add the
htmx.org script, and a button that says click me.  I added just a tish
of style so that it does not sear your delicate developer your eyes.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title></title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
      html  { background: #1f2022; color: #eefbfe; font-size: 64px; }
      button {font-size: 64px;}
      body { height: 100vh; width: 100vw; display: flex; justify-content: center; align-items:center; }
    </style>
    <!-- Load from unpkg -->
    <script src="https://unpkg.com/htmx.org@1.7.0"></script>
  </head>
  <body>
  <!-- have a button POST a click via AJAX -->
  <button hx-get="/partial" hx-swap="outerHTML">
    Click Me
  </button>

  </body>
</html>
```

Save this as `index.html` and fire up a webserver and you will be
presented with this big beefcake of a button.

![big beefcake of a button](https://images.waylonwalker.com/htmx-get-til-click-me.png)

If you don't have a development server preference I reccomend opening
the terminal and running `python -m http.server 8000` then opening your
browser to `localhost:8000`

## The Partial

Now the page has a button that is ready to replace itself, notice the
`hx-swap="outerHTML">`, with the contents of /partial. To create a
static api of sorts we can simply host a partial page in a file at
`/partial/index.html` with the following contents.

```html
<p>
hello
</p>
```

![the final results](https://images.waylonwalker.com/htmx-get-til-hello.png)

<script src="https://unpkg.com/htmx.org@1.7.0"></script>

## Tree

To make it a bit clearer here is what the file tree looks like after
setting this up.

```txt
~/git/htmx  v3.9.7 (git)
❯ tree
.
├── clicked
│   └── index.html
└── index.html
```

## Demo

I added htmx to this page and setup a partial below, check out this
easter egg.

<button hx-get="./partial" hx-swap="outerHTML">
    Click Me
</button>


## Links

* [python web conf 2022](https://2022.pythonwebconf.com/)
* [htmx](https://htmx.org/)
* [big beefcake of a button](https://images.waylonwalker.com/htmx-get-til-click-me.png)
* [the final results](https://images.waylonwalker.com/htmx-get-til-hello.png)
