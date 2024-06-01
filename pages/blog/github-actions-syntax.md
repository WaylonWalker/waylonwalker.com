---
templateKey: blog-post
tags:
- actions
title: Getting Started with GitHub Actions
date: 2020-03-16T05:00:00.000+00:00
published: true
jinja: false

---

Github actions are written in configuration files using the YAML syntax.  YAML
is a superset of JSON.  Most YAML can be expressed inline with JSON syntax.
Similar to python YAML is whitespace driven by whitespace rather than brackets
tags.  The argument for using YAML for configuration files such as actions is
that it is more human-readable and editable.  It's much easier to see the
whitespace layout than it is to get closing brackets correct.  For actions, I
believe this is mostly true.  I don't see any use case to get past 3-5 indents,
which is completely manageable.

> Can I just say that I learned more than I realized about YAML by writing this
> article

## Arrays and Objects

In YAML or JSON, the most basic containers for data are **arrays**, a 1D list
of things, and **objects**, for key-value pairs.

### Arrays

The start of an array container is signified with a leading `-`.  This is
probably one of the big things I didn't understand about YAML before writing
this post, but hats off to the GitHub actions editor as it took care of a lot
of my misunderstanding for me.

``` YAML
- one
- two
- three
```

``` json
['one', 'two', 'three']
```

### Objects

Objects are just `{key: "value"}` pairs without any `-` before them.  I find
that objects make 💯 sense to me.  Unlike arrays, they feel very intuitive.

``` YAML
name: one
who: me
```

``` json
{'name': 'one', 'who': 'me'}
```

## Example Combining arrays and objects

Let's start writing something that looks a bit more like a GitHub action.
GitHub actions are built from an object containing name, on, jobs.  Where jobs
is a list of jobs, that contain a list of steps.  Simple actions will only need
a single job, but commonly a list of steps.

#### Shortlist of GitHub action keys

These are the keys, with their parents, that I found most useful.  You can find
a complete list on
[workflow-syntax-for-github-actions](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions).

* name
* on
	* push
    * pull_request
    * schedule
    * watch
* env
* jobs
	* name
    * needs
    * env
    * if
    * steps

### Combining arrays and objects

Here is a very small example that contains an object with one key, `jobs`.
That `jobs` object contains one job called `build` that contains a list of
`steps`.  Notice the `-` before each step, and how each `step` repeats the same
object keys.

```yaml
jobs:
    build:
        runs-on: ubuntu-latest
        steps:
        - name: step-one
          uses: checkout
        - name: step-two
          uses: test
        - name: step-three
          uses: package
```

``` json
{
  "jobs": {
    "build": {
      "runs-on": "ubuntu-latest",
      "steps": [
        {
          "name": "step-one",
          "uses": "checkout"
        },
        {
          "name": "step-two",
          "uses": "test"
        },
        {
          "name": "step-three",
          "uses": "package"
        }
      ]
    }
  }
}
```

## Multiline Strings

Multiline strings are super important in GitHub actions.  You will likely use
the `|` to preserve newlines for shell scripts most commonly but may also have
some raw text fields that need to be concatenated without a newline character
using the `>` operator.

* | preserves newlines
* > folds newlines

``` YAML
preserved: |
    cd my-dir
    ls
    mv public ../
folded: >
    This is some long text
    that I do not want on
    one line, but it is
    really a one-liner
```

``` JSON
{
    "preserved": "cd my-dir\nls\nmv public ../\n",
    "folded": "This is some long text that I do not want on one line, but it is  really
   a one-liner"
}
```

> 🔥 I always use `|` for steps that are scripts

[[ testproject-io-py-actions ]]

In 👆 This article you can see how I use the `|` character to run some docker
compose commands in a GitHub action to run some integration tests wtih pytet,
testproject.io, a headless browser, and selenium.

## Anchors are not supported

YAML has this amazing feature for reducing repetative content called anchors.
You can save part of your configuration as a reusable variable in other
sections.  I see this being really cool if you had separate jobs that all
needed similar steps.  Look for this improvement in the future, for now just be
aware that it is part of the YAML syntax.

See support ticket 👉
[Support-for-YAML-anchors](https://github.community/t5/GitHub-Actions/Support-for-YAML-anchors/m-p/30336)

``` YAML
secrets: &secrets
    github-pat: ${{ gh-pat }}
    gmail-pass: ${{ gmail-pass }}

jobs:
    build:
        - name: step-one
          uses: checkout
          <<: *secrets
        - name: step-two
          uses: test
          <<: *secrets
        - name: step-three
          uses: package
          <<: *secrets
```

Notice how the nice clean YAML syntax gets exploded with much more data in the
JSON format.

``` json
{
    "secrets": {
        "github-pat": "${{ gh-pat }}",
        "gmail-pass": "${{ gmail-pass }}"
    },
    "jobs": {
        "build": [
            {
                "github-pat": "${{ gh-pat }}",
                "gmail-pass": "${{ gmail-pass }}",
                "name": "step-one",
                "uses": "checkout"
            },
            {
                "github-pat": "${{ gh-pat }}",
                "gmail-pass": "${{ gmail-pass }}",
                "name": "step-two",
                "uses": "test"
            },
            {
                "github-pat": "${{ gh-pat }}",
                "gmail-pass": "${{ gmail-pass }}",
                "name": "step-three",
                "uses": "package"
            }
        ]
    }
}
```

## Writing an Action

With a basic understanding of YAML you can probably go to your repo and click
actions > new workflow > setup my own workflow right from the ui, and create
your own.  Or read through the official syntax docs for deeper information
[workflow-syntax-for-github-actions](https://help.github.com/en/actions/reference/workflow-syntax-for-github-actions).
Let's finsh off with a really simple action, the default one from GitHub.

### Important first step

It is important to know that when running an action you will likely need access
to your code in order to lint, test, build, package, whatever you want to do
with it.  Your first step for any action requiring code from your repo is to
`checkout` your repo.

```yaml
 steps:
 # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
 - uses: actions/checkout@v
```

### Default example

This example runs a workflow called `CI` on ubuntu on every push or PR to the
main branch.  Within the build job it does a checkout of the repo, then runs
two shell steps.

``` YAML
# This is a basic workflow to help you get started with Actions

name: CI

# Controls when the action will run. Triggers the workflow on push or pull request
# events but only for the main branch
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
  # This workflow contains a single job called "build"
  build:
    # The type of runner that the job will run on
    runs-on: ubuntu-latest

    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
    # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
    - uses: actions/checkout@v2

    # Runs a single command using the runners shell
    - name: Run a one-line script
      run: echo Hello, world!

    # Runs a set of commands using the runners shell
    - name: Run a multi-line script
      run: |
        echo Add other actions to build,
        echo test, and deploy your project.

```

[[ four-github-actions-website ]]

## Python

[[ four-github-actions-python ]]

If you are a python deveoper like me you will likely want to use GitHub actions
to Lint, Test, Package, and deploy your python projects. 👆 This article covers just that.
