---
date: 2022-03-14 00:19:02.158919
templateKey: til
title: pytest-mock Basics
tags:
  - python
  - python
  - python

---

Last Thursday I learned about `pytest-mock` at a local python meetup.  The
presenter showed how he uses `pytest-mock` for his work, and it was kinda eye
opening.  I knew what mocking was, but I had not seen it in this context.

## Discovery

Watching him use `pytest-mock` I realized that mocking was not as hard as I had
made it out to be.  You can install `pytest-mock`, use the mocker fixture, and
patch objects methods with what you want them to be.

## install

pytest-mock is out on pypi and can be installed with pip.

```
python -m pip install pytest-mock
```

## What I actually did

Sometimes I fall victim to making these posts nice and easy to follow.  It
takes more steps than just pip install, you need a place to practice in a nice
sandbox.  Here is how I make my sandboxes.

``` python
mkdir ~/git/learn-pytest-mock
cd ~/git/learn-pytest-mock
# well actually open a new tmux session there
echo pytest-mock > requirements.txt

# I copied in my .envrc, and ran direnv allow, which actually just made me a virtual env as follows
python3 -m venv .venv --prompt $(basename $PWD)
source .venv/bin/activate

# now install pytest-mock
pip install -r requirements.txt

# make some tests to mock
mkdir tests
nvim tests/test_me.py
```

## create a tests/test_me.py

I just wanted to do something that was worth mocking, the first thing that came
to mind was to do something that made a network call.  Here I made a method
that uses requests to go get the content on my homepage, but changes it's
return behavior based on the `status_code` of the request.

I want to mock out `requests` to ensure that GoGetter can handle both `200`
(http success) and `404` (http not found) status codes.

``` python
# tests/test_me.py
import requests


class GoGetter:
    """
    The thing I am testing, this is usually imported into the test file, but
    defined here for simplicity.
    """
    def get(self):
        """
        Get the content of `https://waylonwalker.com` and return it as a string
        if successfull, or False if it's not found.
        """
        r = requests.get("https://waylonwalker.com")
        if r.status_code == 200:
            return r.content
        if r.status_code == 404:
            return False


class DummyRequester:
    def __init__(self, content, status_code):
        """
        mock out content and status_code
        """

        self.content = content
        self.status_code = status_code

    def __call__(self, url):
        """
        The way I set this up GoGetter is going to call an instance of this
        class, so the easiest way to make it work was to implement __call__.
        """
        self.url = url
        return self


def test_success_get(mocker):
    """
    Show that the GoGetter can handle successful calls.
    """
    go_getter = GoGetter()

    # Use the mocker fixture to change how requests.get works while inside of test_success_get
    mocker.patch.object(requests, "get", DummyRequester("waylonwalker", 200))
    assert "waylon" in go_getter.get()


def test_failed_get(mocker):
    """
    Show that the GoGetter can handle failed calls.
    """
    go_getter = GoGetter()

    # Use the mocker fixture to change how requests.get works while inside of test_failed_get
    mocker.patch.object(requests, "get", DummyRequester("waylonwalker", 404))
    assert go_getter.get() is False
```
