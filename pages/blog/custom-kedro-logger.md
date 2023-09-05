---
templateKey: blog-post
tags: ['kedro', 'python']
title: Custom Kedro Logger
date: 2021-05-02T09:45:22
published: false

---

DRAFT -



``` yaml
formatters:
    mine:
        format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(me)s"

handlers:

    mine_handler:
        class: logging.StreamHandler
        level: INFO
        formatter: mine
        stream: ext://sys.stdout

loggers:
    me:
        level: DEBUG
        handlers: [mine_handler]

root:
    level: INFO
    handlers: [console, info_file_handler, error_file_handler]
```
