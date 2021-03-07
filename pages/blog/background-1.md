---
templateKey: 'blog-post'
title: background tasks in python
date: 2017-09-16
category: python
tags:
    - python
    - data
description: none

---

# background tasks in python

I have tried most of the different methods in the past and found that copying and pasting the [threadpoolexecutor example](https://docs.python.org/3/library/concurrent.futures.html#threadpoolexecutor-example) or the [processpoolexecutor example](https://docs.python.org/3/library/concurrent.futures.html#processpoolexecutor-example) from the standard library documentation to be the most reliable.  Since this is often something that I stuff in the back of a utility module of a library it is not something that I write often enough to be familiar with, which makes it both hard to write and hard to read and debug.  If you are looking for a good overview of the difference concurrency [Raymond Hettinger](https://twitter.com/raymondh) has a great talk about the difference between the various different methods, when to use them and why.

Recently a new python library was released to make running tasks in the background very simple. The [background](https://github.com/kennethreitz/background) project by Kenneth Reitz is a high level implementation of python 3's ThreadPoolExecutor.  I have been playing around with this project over the last week and I will say that this is definitely the simplest way to run background tasks in python by far.  It really simplifes the syntax and lets me focus on my job rather than implementing custom concurrent code that is more difficult to debug.

## Background

I have pulled the latest version of the project in Sept 2017.  I found that it had some updates that were important to pass \*args and \*\*kwargs compared to the pypi version.


```python
import time
import background as bg

%load_ext watermark
%watermark -d -v -p background
```

    2017-09-16

    CPython 3.6.2
    IPython 6.1.0

    background n


## Define Worker Functions

Each of these worker functions takes 1s to run, simulating a moderately long calculation that we need to do many times over.


```python
def work():
    time.sleep(1)
    return 1

@bg.task
def bg_work():
    time.sleep(1)
    return 1
```

## Run the Worker Functions

## Blocking function

This function is blocking each time the function runs, thus taking 1 second to run for each calculation.  The example below took exactly **100 s** to run 100 calculations.  Depending on your use case this may not be fast enough.  If the calculations do not rely on the global state


```python
%%time
for _ in range(100):
    work()
```

    Wall time: 1min 40s


### Reaction

I  know what half of you are saying to yourselfs..

>    !!What!! that took 100 s, by now my users have already sent a dozen messages and filed an issue that my feature is down

and the other half

> Seriously that wasnt even enough time to grab a coffee.  Any real time consuming analysis takes at least 3 dats 14 hours 159 seconds before I start to care about concurrency

To you I say... I am impatient and I got other things to do rather than wait on this maching to finish its work.  Let's get into this concurrency stuff.

## Background Function

This function spins off worker processes and runs much faster.  By default background sets the number of processes to the number of cpu cores available, Therefore this function should run in n/4 + (inefficiency).  Here we see that the result is just over **13 s**.

Note:_Since there is a bit of inefficiency added by needing to handle all of the threads it is not exactly divided by the number of workers._


```python
%%time
f_list = [bg_work() for _ in range(100)];

while not all([f.done() for f in f_list]):
    pass
```

    Wall time: 13.1 s


### Reaction

I know what your saying this time.

>really a 7.6x improvement...  Is that really even woth the extra work.


Fine then lets crank it up to 11!

### Lots of Background

lets set the number of background processes to a value just higher to than the number of workers we need to run in order to start them all simultaneously. With this simple example that is not very CPU intensive we see the result is just over the amount of time that it takes to run 1 worker.


```python
bg.n = 110
```


```python
%%time
f_list = [bg_work() for _ in range(100)];

while not all([f.done() for f in f_list]):
    pass
```

    Wall time: 1.09 s


### Reaction

> 91x improvement by putting my calculations into a function, adding a decorator, and some checks, im in.

## On Tap

This week while taking it up to 11 I was enjoying a super thick and rich cup of El Salvador Finca Rosa from Onyx Coffee Labs.  Check out their love for letting the bean speak for it self and producing a great cup.

[<img src="https://cdn.shopify.com/s/files/1/1707/3261/files/coffee_science.png?5305428688827820856">](https://onyxcoffeelab.com)
