---
title: '💭 cyclotruc/gitingest: Replace ''hub'' with ''ingest'' in any github...'
date: 2025-01-09T13:46:33
templateKey: link
link: https://github.com/cyclotruc/gitingest
tags:
  - ai
  - llm
  - python
published: true

---

> Gitingest has a python package on pypi that you can run with uvx, and it accepts the same arguments as the web version, right in your terminal


``` bash
⬢ [devtainer] ❯ uvx gitingest --help
Usage: gitingest [OPTIONS] SOURCE

  Analyze a directory and create a text dump of its contents.

Options:
  -o, --output TEXT           Output file path (default: <repo_name>.txt in
                              current directory)
  -s, --max-size INTEGER      Maximum file size to process in bytes
  -e, --exclude-pattern TEXT  Patterns to exclude
  -i, --include-pattern TEXT  Patterns to include
  --help                      Show this message and exit.
```

[Original thought](https://github.com/cyclotruc/gitingest)
