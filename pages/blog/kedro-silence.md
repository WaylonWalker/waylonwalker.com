---
templateKey: blog-post
tags: ['kedro', 'python']
title: Silence Kedro Logs
date: 2021-04-02T00:00:00 
status: draft

---



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

## Get

Getting a python logger is straightforward if we know the name of the logger.
The following block will grab the logger object for the logger currently
registered under the name passed in.

``` python
logger = logging.getLogger('kedro')
```

## Set Level

Once we get the logger we need to silence it by setting the log level.
Typically its not appropriate to completely turn off loggers as you would still
want information in the case of a complete failure.  If you are doing building
a cli such as one that prints out the pipelines to the console you may not want
to see logs that happen during normal operation as this would make it more
difficult to integrate with other shell applications.

``` python 
logger.setLevel(logging.ERROR)
```

> Note: it is possible to set the log level before kedro even registers the
> logger, if there is no logger currently setup under getLogger, it will create
> one.

## Silent all kedro loggers

As of `kedro==0.17.3` This function covers every logger that is issued by
kedro.  I generated this list of `known_kedro_loggers` by looking through their
codebase and filling in a few  others I found by running it.

``` python
def silent_loggers() -> None:
    """All logs need to be silent in order for a clean kedro diff output."""
    known_kedro_loggers = [
        "ProfileTimeTransformer",
        "hooks_handler",
        "kedro.__init__",
        "kedro",
        "kedro.config",
        "kedro.config.config",
        "kedro.extras.decorators.memory_profiler",
        "kedro.framework.cli",
        "kedro.framework.session.session",
        "kedro.framework.session.store",
        "kedro.framework.session",
        "kedro.io.cached_dataset",
        "kedro.io.data_catalog",
        "kedro.io",
        "kedro.journal",
        "kedro.pipeline",
        "kedro.pipeline.decorators",
        "kedro.pipeline.node",
        "kedro.pipeline.pipeline",
        "kedro.runner",
        "kedro.runner.runner",
        "kedro.versioning.journal",
        "py4",
    ]
    for logger in [
        *known_kedro_loggers,
        *list(logging.root.manager.loggerDict.keys()),  # type: ignore
    ]:
        logging.getLogger(logger).setLevel(logging.ERROR)
```
