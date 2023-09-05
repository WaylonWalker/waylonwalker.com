---
date: 2023-01-23 10:52:19
templateKey: til
title: Releasing a New Version of Your Python Package Just Got Easier
published: true
tags:
  - cli
---

Quickly and easily create new versions of your Python package with the `gh release`
command. Get the version number, changelog, and

Releasing a new version of your Python package can be a daunting task. You need to make
sure that all the necessary files are included, and that the version number is correct.
But now, with the help of the `gh release` command, you can make the process much
smoother.

The `gh release` command allows you to quickly and easily create a new version of your
Python package. All you need to do is provide the version number, the changelog, and the
distribution files. For example, if you wanted to create a new version of your package
with the version number `v1.2.3`, you could use the following command:

```bash
gh release create v1.2.3 -F CHANGELOG.md dist/*.whl dist/*.tar.gz
```

This command will create a new version of your package with the specified version number,
and include the changelog and the distribution files. It's a great way to make sure that
all the necessary files are included in the release, and that the version number is
correct.

The `gh release` command is a great tool for quickly and easily creating new versions of
your Python package. With just a few simple commands, you can make sure that all the
necessary files are included, and that the version number is correct. So if you're looking
for an easy way to release a new version of your Python package, give the `gh release`
command a try.
