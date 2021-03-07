---
templateKey: blog-post
related_post_label: Check out this related post
tags:
- actions
title: Four github actions for your website
date: 2020-05-18T13:02:00.000+00:00
status: published
description: GitHub actions can give you confidence that your site is up and running,
  with the latests JavaScript packages, does not have broken links, and can even take
  screenshots of what your website looks like on different screen sizes and operating
  systems.
cover: "/static/four-github-actions-website.png"

---
GitHub's actions are a new GitHub feature that will trigger GitHub to spin up a virtual machine and run some tasks with some special access to your repo. It can interact with comments/issues, it can clone your repo, You can explicitly pass in secrets so that it can commit back to the repo or deploy to another service. The environment may be a Linux, windows, or even a mac machine. I believe this is wildly incredible for the open-source community, putting these tools in the same place that we are already collaborating is so convenient.

## What can they do for my personal website? 🤔

GitHub actions can give you confidence that your site is up and running, with the latest JavaScript packages, does not have broken links, and can even take screenshots of what your website looks like on different screen sizes and operating systems.

- periodically check that the website is up
- update npm
- url checker
- screenshot website


## [srt32/uptime](https://github.com/srt32/uptime)

[srt32/uptime](https://github.com/srt32/uptime) is an action that you can run on any public website. I run this one several times every day and it gives me confidence that my various sites are still up and running. It ensures that my build didn't break something, nothing is wrong with my hosting provider, or my DNS.

``` yaml
name: check if site is up
on:
  schedule:
    - cron: '0 0 * * *'

jobs:
  ping_site:
    runs-on: ubuntu-latest
    name: Ping the site
    steps:
    - name: Check the site
      id: hello
      uses: srt32/uptime@master
      with:
        url-to-hit: "https://waylonwalker.com/"
        expected-statuses: "200,301"
```

## [taichi/actions-package-update](https://github.com/taichi/actions-package-update)

Here is another one to make sure that your package.json does not get too far out of date, or have any vulnerabilities. [taichi/actions-package-update](https://github.com/taichi/actions-package-update) will submit a PR back to your repo with any updated dependencies. Since it submits it as a pr, your tests triggered by PRs should also run. giving you confidence that you are ready to update.

<p style='text-align: center'>
<img src='https://github.com/taichi/actions-package-update/raw/master/docs/actions-package-update.png' style='width:600px; max-width:80%; margin: auto;' alt='image of a PR submitted by actions-package-update'/>
</p>

Example to update `package.json` every Wednesday night at midnight.

``` yaml
on:
  schedule:
  - cron: 0 0 * * 3
name: Update
jobs:
  package-update:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@master
    - name: set remote url
      run: git remote set-url --push origin https://$GITHUB_ACTOR:${{ secrets.GITHUB_TOKEN }}@github.com/$GITHUB_REPOSITORY
    - name: package-update
      uses: taichi/actions-package-update@master
      env:
        AUTHOR_EMAIL: john@example.com
        AUTHOR_NAME: john
        EXECUTE: "true"
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        LOG_LEVEL: debug
      with:
        args: -u --packageFile package.json --loglevel verbose
```

## [urlstechie/urlchecker-action](https://github.com/urlstechie/urlchecker-action)

[urlstechie/urlchecker-action](https://github.com/urlstechie/urlchecker-action) is an action to collect and check URLs in a project and report on broken links. This is another one to give yourself some confidence that you are not linking out to a broken site, and can give you a heads up before you have frustrated users.

``` yaml
name: Check URLs

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: urls-checker
      uses: urlstechie/urlchecker-action@0.2.1
      with:
        # A subfolder or path to navigate to in the present or cloned repository
        subfolder: docs

        # A comma-separated list of file types to cover in the URL checks
        file_types: .md,.py,.rst

        # Choose whether to include file with no URLs in the prints.
        print_all: false

        # The timeout seconds to provide to requests, defaults to 5 seconds
        timeout: 5

        # How many times to retry a failed request (each is logged, defaults to 1)
        retry_count: 3

        # A comma separated links to exclude during URL checks
        white_listed_urls: https://github.com/SuperKogito/URLs-checker/issues/1,https://github.com/SuperKogito/URLs-checker/issues/2

        # A comma separated patterns to exclude during URL checks
        white_listed_patterns: https://github.com/SuperKogito/Voice-based-gender-recognition/issues

        # choose if the force pass or not
        force_pass : true
```

## [swinton/screenshot-website](https://github.com/swinton/screenshot-website)

[swinton/screenshot-website](https://github.com/swinton/screenshot-website) will take a screenshot of your website. It can even run a matrix of sizes and os's to check how your site looks on various systems.

``` yaml
name: screenshot-website
on:
  schedule:
    - cron: '0 0 0 * *'

jobs:
  screenshot:
    name: Screenshot
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
        width: [1200, 992, 768, 600]
    runs-on: ${{ matrix.os }}

    steps:

    - name: Screenshot Website
      uses: swinton/screenshot-website@v1.x
      with:
        source: https://waylonwalker.com/
        destination: screenshot-${{ matrix.os }}-${{ matrix.width }}.png
        width: ${{ matrix.width }}
```
