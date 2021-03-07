---
templateKey: blog-post
related_post_label: Check out this related post
tags: ['python',]
title: Integration testing with Python, TestProject.io, and GitHub Actions
date: 2020-07-27T05:00:00Z
status: published
description: As I continue to build out
    https://waylonwalker.com/ I sometimes run into some
    errors that are not caught becuase I do not have good testing implemented. I
    want to explore some integration testing options using GitHub actions.
cover: /static/testproject-io-py-actions.png

---

As I continue to build out [waylonwalker.com](https://waylonwalker.com/) I sometimes run into some errors that are not caught because I do not have good testing implemented.  I want to explore some integration testing options using GitHub's actions.

Running integration tests will not prevent bugs from happening completely, but it will allow me to quickly spot them and rollback.


---

## 🤔 What to test first?

The very first thing that comes to my mind is anything that is loaded or ran client-side.  Two things quickly came to mind here.  I run gatsby so most of my content is statically rendered, and it yells at me if something isn't as expected.  For performance reasons I lazy load cards on my blogroll, loading all of the header images gets heavy and kills lighthouse (if anyone actually cares). I am also loading some information from the top open-source libraries that I have created.  To prevent the need to rebuild the whole site to get the latest information I am just using the GitHub API client-side.


things I was looking for from features to test

* client-side interactions
* external API

features on my blog to consider testing

* lazy-loaded blog cards
* GitHub Repos


## Repo Cards

I chose to start with the GitHub repos as they seemed a bit more straight forward, and it's been a while since I have done any selenium.

<p style='text-align: center'>
<img src='https://images.waylonwalker.com/open-source-cards.png' style='width:600px; max-width:80%; margin: auto;' alt='Open Source cards as they look on waylonwalker.com'/>
</p>

> here is what the GitHub repo cards look like

## TestProject.io

I am trying out [TestProject.io](https://TestProject.io) for the first time on this project.  My experience so far has been top-notch.  There was an existing suite of docker images/files set up to run the TestProject agent in a docker container alongside headless chrome and firefox drivers.  The first thing that you are going to need is a [TP\_DEV\_TOKEN ](https://app.TestProject.io/#/integrations/sdk) and [TP\_API\_KEY](https://app.TestProject.io/#/integrations/api).  These will give TestProject access to your account so that it can automatically post results to your [dashboard](https://app.TestProject.io/#/reports)

* [TP\_DEV\_TOKEN ](https://app.TestProject.io/#/integrations/sdk)
* [TP\_API\_KEY](https://app.TestProject.io/#/integrations/api)

### Put these in secrets in your repo

In your GitHub repo go to `settings>Secrets`, or append `settings/secrets` to the URL to your repo, and add the tokens.  This will give GitHub safe access to them without them being available to the public, contributors, log files, or anything.


<p style='text-align: center'>
<img src='https://images.waylonwalker.com/test-waylonwalker-com-secrets.png' style='width:600px; max-width:80%; margin: auto;' alt='Secrets panel in the GitHub Repo'/>
</p>


## Setup Dev

To expedite development I went ahead and set up development environment that I could log into on Digital Ocean.  This allowed me to get all of my tests working a bit quicker than just running them through GitHub, but being as similar as possible.  This allowed me to learn the ins and outs of setting up TestProject without needing to do a full install every time through Github's actions.

<p style='text-align: center'>
<a href='https://waylonwalker.com/notes/new-machine-tpio'>
  <img
    style='width:500px; max-width:80%; margin: auto;'
    src="https://images.waylonwalker.com/new-machine-tpio-rm.png"
    alt="Test Project Dev Machine setup notes card"
  />
  </a>
</p>

> I am not going to go into full dev machine setup here, but you can read my [setup notes](https://waylonwalker.com/notes/new-machine-tpio).

## 🐍 Pytest
_you can see all of the tests ran with pytest on [github](https://github.com/waylonwalker/waylonwalker-com-tests/tree/master/tests)_

I chose to go down the route of using pytest.  I really liked the idea of utilizing fixtures, automatically running my test functions, and utilizing a bit of the pytest reporting capabilities.

**NOTE** per pytest standard practice I named the directory containing tests `tests`.  While this works, TestProject.io uses this director as the default name for the project.  If I were to go back I would either rename the directory to what I want to show up on TestProject.io or configure the project name inside of the config.


## conftest.py
_You can see the [conftest.py](https://github.com/WaylonWalker/waylonwalker-com-tests/blob/master/tests/conftest.py) live on GitHub._


pytest automatically imports [conftest.py](https://github.com/WaylonWalker/waylonwalker-com-tests/blob/master/tests/conftest.py) modules from the same directory that you are working from.  It's common to place fixtures used across multiple files here.  I placed a driver fixture in this module so that as I create more tests it will be available everywhere by default.

> conftest.py stores fixtures for all modules in a directory.

``` python
# tests/conftest.py

import time
import pytest
from src.TestProject.sdk.drivers import web driver

@pytest.fixture
def driver():
    "creates a webdriver and loads the homepage"
    driver = webdriver.Chrome()
    driver.get("https://waylonwalker.com/")
    yield driver
    driver.quit()
```
> Look at the full version of [conftest.py](https://github.com/WaylonWalker/waylonwalker-com-tests/blob/master/tests/conftest.py)

The above sample is a bit **simplified**.  I ran into some inconsistencies in the real version and found that some tests had a better pass rate if I added a wait.  I ended up with a `driver` and a `slow_driver` fixture.

## test_repos.py

_see the full [testrepos.py](https://github.com/WaylonWalker/waylonwalker-com-tests/blob/master/tests/test_repos.py) on GitHub_


I have initially set up 3 different tests for the repo cards.  I set a list of repos that I expect to show up in the cards.  These tests are quite easy to do with TestProject.io as it is using selenium and a headless browser to execute javascript under the hood.

If you are not familiar a **headless browser** runs the engine as your browser without a graphical user interface.  JavaScript gets fully loaded and parsed, and the dom is completely interactive programmatically.

``` python
"""
Test that GitHub repo data dynamically loads the client-side.
"""

REPOS = [
    "find-kedro",
    "kedro-static-viz",
    "kedro-action",
    "steel-toes",
]

def test_repos_loaded(slow_driver):
    """
    Test that each repo-name exists as a title in one of the repo cards.

    On waylonwalker.com repo cards have a title with a class of "repo-name"
    """
    repos = slow_driver.find_elements_by_class_name("repo-name")
    # get innertext from elements
    header_text = [
        header.text for header in repos
    ]
    for repo in REPOS:
        assert repo in header_text


def test_repo_description_loaded(slow_driver):
    """
    Test that each repo has a description longer than 10 characters

    On waylonwalker.com repo cards have a descriptiion with a class of "repo-description"
    """
    repo_elements = slow_driver.find_elements_by_class_name("repo")
    for el in repo_elements:
        desc = el.find_element_by_class_name("repo-description")
        assert len(desc.text) > 10


def test_repo_stars_loaded(slow_driver):
    """
    Ensure that stars are properly parsed from the API and loaded client-side

    On waylonwalker.com repo cards have a stars element with a class of "repo-stars" and
    is displayed as "n stars"
    """
    repo_elements = slow_driver.find_elements_by_class_name("repo")
    for el in repo_elements:
        stars = el.find_element_by_class_name("repo-stars")
        num_stars, label = stars.text.split()
        assert int(num_stars) > 0
        assert label == 'stars'
```

## Forum
_[forum.TestProject.io](https://forum.TestProject.io/t/install-agent-inside-github-actions/2334/3)_

Before jumping into the real action.  I quickly wanted to mention the **amazing** ✨  discord server that they have going.

I was a bit confused about how to set up TestProject.io inside of actions.  I was with a prompt response linking me to the exact example I needed.  The tests were written in java, but they had set up the docker-compose steps that I needed.


---

## GitHub Actions 🎬

_[test-waylonwalker-com.yml](https://github.com/WaylonWalker/waylonwalker-com-tests/blob/master/.github/workflows/test-waylonwalker-com.yml)_

GitHub actions are a continuous integration, continuous delivery service by GitHub that will spin up a VM and run a set of steps upon a number of triggers including push, pull request, and schedule.
---

<p style='text-align: center'>
<a href='https://waylonwalker.com/github-actions-syntax'>
  <img
    style='width:500px; max-width:80%; margin: auto;'
    src="https://images.waylonwalker.com/github-actions-syntax-rm.png"
    alt="GitHub Actions Syntax article card"
  />
  </a>
</p>

> If you're new to actions check out this article on using actions.

---

Now that I have my GitHub repo setup with my [tests](https://github.com/WaylonWalker/waylonwalker-com-tests/tree/master/tests) successfully running in pytest, let's get it running inside of GitHub actions automatically.

``` yaml
name: Test WaylonWalker.com

# Controls when the action will run. Triggers the workflow on push or pull request
# events but only for the master branch
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
  schedule:
    - cron: '*/10 * * * *'
```

You can see in the section above I have set up to run every time there is a push to or pull request open to main.  I also set a fairly aggressive test schedule to run every **10** **minutes**.  For now, this is just to build confidence in the tests and get more data in the reports to explore.  I will likely turn this down later.

``` yaml

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@main
    - uses: actions/setup-python@v2
      with:
        python-version: '3.8'
    - run: pip install -r requirements.txt
    - name: Run TestProject Agent
      env:
        TP_API_KEY: ${{ secrets.TP_API_KEY }} # < Let Secrets handle your keys
      run: |
        envsubst < .github/ci/docker-compose.yml > docker-compose.yml
        cat docker-compose.yml
        docker-compose -f docker-compose.yml up -d
    - name: Wait for Agent to Register
      run: bash .github/ci/wait_for_agent.sh
    - run: pytest
      env:
        TP_DEV_TOKEN: ${{ secrets.TP_DEV_TOKEN }} # < Let Secrets handle your tokens
        TP_AGENT_URL: http://localhost:8585
```

In the test job you can see that we have rendered the [TP\_API\_KEY](https://app.TestProject.io/#/integrations/api) into the [docker-compose.yml](https://github.com/WaylonWalker/waylonwalker-com-tests/blob/master/.github/ci/docker-compose.yml) using `envsubst` file so that TestProject has access to it.  We have also exposed our [TP\_DEV\_TOKEN ](https://app.TestProject.io/#/integrations/sdk) to pytest.


## docker-compose.yml

_[docker-compose.yml](https://github.com/WaylonWalker/waylonwalker-com-tests/blob/master/.github/ci/docker-compose.yml)_

The following [docker-compose.yml](https://github.com/WaylonWalker/waylonwalker-com-tests/blob/master/.github/ci/docker-compose.yml) file was graciously contributed by [@vitalybu](https://github.com/vitalybu) in the [testproject-io/java-sdk](https://github.com/testproject-io/java-sdk/blob/master/.github/ci/docker-compose.yml) repo.  It sets up a template with the **`TP_API_KEY`** as a variable for envsubst, headless browsers for chrome and firefox, and the TestProject.io agent.

``` yaml
version: "3.1"
services:
  testproject-agent:
    image: testproject/agent:latest
    container_name: testproject-agent
    depends_on:
      - chrome
      - firefox
    environment:
      TP_API_KEY: "${TP_API_KEY}"
      TP_AGENT_TEMP: "true"
      TP_SDK_PORT: "8686"
      CHROME: "chrome:4444"
      CHROME_EXT: "localhost:5555"
      FIREFOX: "firefox:4444"
      FIREFOX_EXT: "localhost:6666"
    ports:
    - "8585:8585"
    - "8686:8686"
  chrome:
    image: selenium/standalone-chrome
    volumes:
      - /dev/shm:/dev/shm
    ports:
    - "5555:4444"
  firefox:
    image: selenium/standalone-firefox
    volumes:
      - /dev/shm:/dev/shm
    ports:
    - "6666:4444"
```

## ⌚ Waiting for the Agent to register
_[wait for agent.sh](https://waylonwalker.com/waitforagent.sh)_

I think the most interesting part of the workflow above is how we wait for the agent to register.  The shell script is a bit terse, but it looks for exceeding the `max_attempts` allowed or that the agent has started by using its `/api/status` rest API.  This prevents us from wasting too much time by setting a big wait, or trying to move on too early and running pytest without a running agent.

``` bash
trap 'kill $(jobs -p)' EXIT
attempt_counter=0
max_attempts=100
mkdir -p build/reports/agent
docker-compose -f docker-compose.yml logs -f | tee build/reports/agent/log.txt&
until curl -s http://localhost:8585/api/status | jq '.registered' | grep true; do
    if [ ${attempt_counter} -eq ${max_attempts} ]; then
    echo "Agent failed to register. Terminating..."
    exit 1
    fi
    attempt_counter=$(($attempt_counter+1))
    echo
    sleep 1
done
```


## TestProject.io Dashboard 〽

One one of the coolest features that you get from TestProject.io are the [reports](https://app.testproject.io/#/reports) dashboard.  To me, this felt like a premium feature for **free**.  Here you can see a time-series plot of your tests success rate over time.  It gives you a bit of an ability to slice in, but not a lot.  Some of the filters are pre-canned, like the past 2 days are past 30 days cannot be customized.

<p style='text-align: center'>
  <img
    style='width:800px; max-width:80%; margin: auto;'
    src="https://images.waylonwalker.com/tpio-test-repos.png"
    alt="My Dashboard for test_repos"
  />
</p>

## A single test flow in the dashboard

As you drill in you can see individual tests that have been run, select them, and see individual reports for each test.  Personally I really like the layout on the side.  It converts the steps ran by the driver into a human-readable _flowchart_, and each step can be opened up to see their values.  It would be nice if it picked up my pytest assertions, but picking up what it did was great.


<p style='text-align: center'>
  <img
    style='width:350px; max-width:80%; margin: auto;'
    src="https://images.waylonwalker.com/test_repo_stars_loaded.png"
    alt="driver flow of test_repo_stars_loaded"
  />
</p>


## Overall 😄
The experience I had setting up TestProject.io to run inside GitHub's actions was great.  It was fairly simple to set up and get running with many of the greatest integration testing tools of today, selenium, chrome, firefox.

Now I am going to turn the test frequency down a bit.

---

## More Actions

If you're new to actions check out this article on using actions.

<TABLE>
<TR>
   <TD>
      <a href='https://waylonwalker.com/four-github-actions-website'>
      <img
         style='margin: auto; float: left'
         src="https://images.waylonwalker.com/four-github-actions-website-rm.png"
         alt="GitHub Actions Syntax article card"
         />
      </a>
   </TD>
   <TD>
      <a href='https://waylonwalker.com/four-github-actions-python'>
      <img
         style='margin: auto; float: right;'
         src="https://images.waylonwalker.com/four-github-actions-python-rm.png"
         alt="GitHub Actions Syntax article card"
         />
      </a>
   </TD>
</TR>
