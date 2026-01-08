---
date: 2023-12-22 08:49:07
templateKey: blog-post
title: thoughts on unit tests
tags:
  - python
published: True

---

![thoughts on unit tests cover image](https://images.waylonwalker.com/thought-on-unit-tests.png)

<audio controls="controls">
  <source type="audio/mp3" src="https://dev-app.fokais.com/voice?url=https://waylonwalker.com/thoughts-on-unit-tests/"></source>
  <p>Your browser does not support the audio element.</p>
</audio>

Theo's response puts a lot of my feelings about unit testing into words.  Many
of us have grown up in this world preaching unit testing.  We often hear these
statements "Everything must be unit tested, tests make code more maintainable."
In reality when we are not writing complex low level code unit tests are
probably the wrong approach.

[![thought 192, a thought about theo's reaction to prime's unit testing](https://shots.waylonwalker.com/shot/?url=https%3A%2F%2Fthoughts.waylonwalker.com%2Fpost-og%2F192&height=640&width=1280&scaled_width=1280&scaled_height=640&selectors=)](https://thoughts.waylonwalker.com/post/192)

## Most of us are assemblers

So much of software engineering is assembling existing well tested code. Crud
applications, UI, Data Pipelines, building on top of battle tested code.

## Manufacturing Analogy - Unit Testing

This kind of reminds me of Manufacturing.  Individual components are QA tested
with tests that look more like unit test.  Parts like bearings, pistons,
shafts, valves, they are all tested against sophisticated statistics of sample
measurements.  This is quite similar to unit testing.

![a qa engineer meticulously checking the size of a bearing](https://images.waylonwalker.com/gaugelab.png)

You see measuring the individual sizes of these components does not guarantee
the actual function of the component.  Before the Henry Ford assembly line
parts like this were all different sizes, and they were all custom matched to
each other. The one industry that I can thing of that still exists today like
this is gunsmithing.  parts are made very close to size, but they need some
lapping and final finishing for high quality function.

### Integration Testing

So how are pumps, engines, valve assemblies, and so on tested?  They are
integration testsed based on their function.  They are not generally unit
tested to measurements of thier size.  A pump is tested on a test bench and
will be required to output a spec flow, a valve will have air or fluid applied
and tested for leaks.  An engine is a more complicated case where it will be
ran on a suite of cycles and should output a spec level of power, while
emissions, temperature, fuel consumption and hundreds of other measurements
stay within their specs.

![A large engine sitting on a test bench](https://images.waylonwalker.com/engine-testing.png)

## As assemblers we should be thinking of integration testing

There is 100% a place for unit testing in the software engineering industry,
just like manufacturing, but I don't think it makes sense everywhere.  Library
development and lower level algorithms look a lot more like parts that can be
physically measured. But that's probably not the code most of us are writing
most of the time.

We are likely assembling a lot of code to build a product such as a data
pipeline, or a web application for instance.  For these cases we should be
thinking about the final function of the product.  Like Prime says in the
video, think of the product as a black box, as if you have no idea how anything
works in the box, but you know how it should function.

I'm starting to lean more into simple tools for this qa work on we applications
that I build.  They are easy to build and maintain, and do not get in the way
when the direction of the project changes.  If I rip out half my code it would
be likely to see 3/4's of my unit tests failing.  Not a fun thing to maintain.

## Uptime

This is the simplest form of integration testing that I am pulling into fokais,
and it's nearly fully automatable without much thought on my behalf.  I am
building web applications in fastapi, these api's have endpoints that should be
reachable.  Tools like Uptime Kuma make it trivial to pull in all of my
endpoints and simply ask if they are reachable once per minute.

With uptime tests I can more confidently move through dev to prod.  If dev has
been running for a number of minutes and alarms are not going off, it's probably
functioning.

## Functionality Testing

I've used tools built upon selenium in the past, such as testproject.io.  It is
a pretty great experience, and makes it pretty easy to define, when a user logs
into the dev app, and clicks the dashboard, can they see their name and account
information.

These tests are likely to remain true for the life of the project.  No matter
what changes inside the black box, when a user goes to their account they
should see their account information.  It might be server rendered with jinja,
fetch with htmx, or client side rendered with reactjs, it does not matter.

## Load Testing

The last thing I want to really put as a tool in my toolbelt is load testing.
It's pretty easy to degrade the experience of a webpage with a bad database
query or api call.  Load testing can ensure that your application can handle
the load that you want it to in dev before you release to prod.  I am looking
into bringing in [Locust.io](https://locust.io/) for load testing fokais.com.

## Logging and Monitoring

Inevitably users will use your product in ways that were never intended. It
will be nearly impossible to cover everything with any sort of test.  This is
where logging and monitoring come in.  If you can set up error monitoring and
alerts, then you can check production logs to see what the heck happend and
potentially resolve the issue.  Without monitoring, you will have wild bugs
that you never thought could exist.

![An engine being used in ways unimaginable by the manufacturer being pushed to it's breaking point.](https://images.waylonwalker.com/engine-failure.png)

## Unit Tests are not a Golden fix all

No tests will never be perfect, they will not catch everything.  The point that
I was inspired to make after watching
[Theo's video](https://www.youtube.com/watch?v=MbU-PKukdMw)
is that unit tests may not the right thing for your product, and then requiring
coverage metrics on PR may be more of a detriment to the product than help.
