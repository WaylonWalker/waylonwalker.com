---
date: 2022-09-01 13:19:22
templateKey: til
title: Versioning Python Projects with Hatch
status: 'published'
tags:
  - python
cover: https://images.waylonwalker.com/hatch-version.png

---

Hatch has an amazing versioning cli for python packages that just works.  It
takes very little config to get going and you can start bumping versions
without worry.

## project layout

For trying out the `hatch version` cli let's make a simple project with the
terrible name `pkg`.

``` bash
❯ tree .
.
├── pkg
│   ├── __about__.py
│   └── __init__.py
├── pyproject.toml
└── README.md

1 directory, 4 files
```

## pyproject.toml

The main hero of this post is the `pyproject.toml`.  This is what defines all
of our [PEP 517](https://peps.python.org/pep-0517/) style project setup.

``` toml
[project]
name = "pkg"
description = "Show how to version packages with hatch"
readme = "README.md"
dynamic = [
 "version",
]

[build-system]
requires = [
 "hatchling>=1.4.1",
]
build-backend = "hatchling.build"

[tool.hatch.version]
path = "pkg/__about__.py"
```

## statically versioning
_project.version_

It is possible to set the version number inside the `pyproject.toml`
statically.  This is fine if you just want to version your package manually,
and not through the `hatch` cli.

``` toml
[project]
name = "pkg"
version = "0.0.0"
# ...
```

> Statically versioning in pyproject.toml will not work with `hatch version`

![hatch-static-version-error](https://screenshots.waylonwalker.com/hatch-static-version-error.webp)

``` bash
Cannot set version when it is statically defined by the `project.version` field
```

## dynamically Versioning
_project.dynamic_

Setting the project verion dynamically can be done by changing up the following
to your `pyproject.toml`.  Hatch only accepts a path to store your version.  If
you need to reference  it elsewhere in your project you can grab it from the
package metadata for that file.  I would not put anything else that could
possibly clash with the version, as you might accidently change both things.

If you really need to set it in more places use a package like bump2version.

``` toml
[project]
name = "pkg"
dynamic = [
  "version"
]
# ...
[tool.hatch.version]
path = "pkg/__about__.py"
```

> Note: you can configure hatch to use a different pattern
> https://hatch.pypa.io/1.2/version/#configuration, but I have not found it to
> be something that I need.

## __about__.py

The [hatch](https://github.com/pypa/hatch/) project itself uses a
[__about__.py](https://github.com/pypa/hatch/blob/master/src/hatch/__about__.py)
to store it's version. It's sole content is a single `__version__` variable.  I
don't have any personal issues with this so I am going to be following this in
my projects that use hatch.


``` python
__version__ = "0.0.0"
```

## versioning
_[hatch version docs](https://hatch.pypa.io/1.2/version/#updating)_

Hatch has a pretty intuitive versioning api.  `hatch version` gives you the
version.  If you pass in a version like `hatch version "0.0.1"` it will set it
to that version as long as it is in the future, otherwise it will error.

``` bash
# print the current version
hatch version

# set the version to 0.0.1
hatch version "0.0.1"
```

## bumping

You can bump parts of the [semver](https://semver.org/) version.

``` bash
# minor bump
hatch version minor

# beta pre-release bump
# If published to pypi this can be installed with the --pre flag to pip
hatch version b

# bump minor and beta
hatch version minor,b

# release all of the --pre-release flags such as alpha beta rc
hatch release
```

## Example

Here is a screenshot of bumping a projet along.

![hatch-version-cli](https://screenshots.waylonwalker.com/hatch-version-cli.webp)

## GitOps

In my github actions flow I will be utilizing this to automate my versions. In
my side projects I use the `develop` branch to release --pre releases.  I have
all of my own dependent projets running on these --pre releases, this allows me
to cut myself in my own projects before anyone else.  Then on main I
automatically release this beta version.

## GitHub Actions

Here is what the ci/cd for `markata` looks like. There  might be a better
workflow strategy, but I use a single github actions workflow and cut branches
to release --pre releases and full release.  These steps will bump, tag,
commit, and deploy for me.

``` yaml
      - name: automatically pre-release develop branch
        if: github.ref == 'refs/heads/develop'
        run: |
          git config --global user.name 'autobump'
          git config --global user.email 'autobump@markata.dev'
          VERSION=`hatch version`
          # if current version is not already beta then bump minor and beta
          [ -z "${b##*`hatch version`*}" ] && hatch version b || hatch version minor,b
          NEW_VERSION=`hatch version`
          git add markta/__about__.py
          git commit -m "Bump version: $VERSION → $NEW_VERSION"
          git tag $VERSION
          git push
          git push --tags

      - name: automatically release main branch
        if: github.ref == 'refs/heads/main'
        run: |
          git config --global user.name 'autobump'
          git config --global user.email 'autobump@markata.dev'
          VERSION=`hatch version`
          hatch version release
          NEW_VERSION=`hatch version`
          git add markta/__about__.py
          git commit -m "Bump version: $VERSION → $NEW_VERSION"
          git tag $VERSION
          git push
          git push --tags

      - name: build
        run: |
          python -m build

      - name: pypi-publish
        if: github.ref == 'refs/heads/develop' || github.ref == 'refs/heads/main'
        uses: pypa/gh-action-pypi-publish@v1.1.0
        with:
          password: ${{ secrets.pypi_password }}
```

## Hatch Version Action

I am setting up a github custom action
[waylonwalker/hatch-version-action](https://github.com/WaylonWalker/hatch-version-action)
that will lint, test, bump, and publish for me in one step.  More on that in
the future.
