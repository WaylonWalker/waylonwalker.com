---
templateKey: blog-post
tags: ['kedro', 'python']
title: Silence Kedro Logs - DRAFT
date: 2021-04-02T00:00:00 
status: published

---

DRAFT

Kedro can have a quite chatty logger.  While this is super nice in production
so see everything that happened during a pipeline run, this can be troublesome
while trying to implement a cli extension with clean output.

## Silence a Python log

First how does one silence a python log?  Python loggers can be retrieved by
the `logging` modules `getLogger` function, then their log level can be
changed.  Much of kedro's chattyness comes from INFO level logs.  For my
current use case I don't want to hear about anything unless its really
important, i.e. there was a failure.  In this case I am going to set the log
levels to ERROR as most errors should stop execution anyways.


### python logging levels


| Level    | Numeric value |
|----------|---------------|
| CRITICAL | 50            |
| ERROR    | 40            |
| WARNING  | 30            |
| INFO     | 20            |
| DEBUG    | 10            |
| NOTSET   | 0             |

## Gett
