---
templateKey: blog-post
tags: [ 'python']
title: Pytest capsys
date: 2021-04-05T08:46:08
status: published

---

Testing print/log statements in pytest can be a bit tricky, capsys makes it
super easy, but I often struggle to find it.


## capsys

capsys is a builtin pytest fixture that can be passed into any test to capture
stdin/stdout.  For a more comprehensive description check out the docs on
[capsys](https://docs.pytest.org/en/stable/capture.html#accessing-captured-output-from-a-test-function)

## using capsys

Simply create a test function that accepts capsys as an argument and pytest
will give you a capsys opject.

``` python
def test_print(capsys):
    print('hello')
    captured = capsys.readouterr()
    assert 'hello' in captured.out
    print('world')
    captured = capsys.readouterr()
    assert 'world' in captured.out
```
