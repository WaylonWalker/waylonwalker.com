---
date: 2022-01-08 01:16:52.790764
templateKey: til
title: Copier Answers
tags:
  - python
  - linux
  - cli

---

The copier answers file is a key component to making your templates re-runnable.

``` bash
❯ tree ~/.copier-templates/setup.py
/home/walkers/.copier-templates/setup.py
├── [[ _copier_conf.answers_file ]].tmpl
├── copier.yml
├── setup.cfg
└── setup.py.tmpl

0 directories, 4 files
```

``` yaml
# ~/.copier-templates/setup.py/\[\[\ _copier_conf.answers_file\ \]\].tmpl
# Changes here will be overwritten by Copier; NEVER EDIT MANUALLY
[[_copier_answers|to_nice_yaml]]
```

``` yaml
# copier.yml
package_name:
author_name: Waylon Walker
author_github: waylonwalker
description:
framework:
  choices:
    - '"Framework :: Kedro",'
    - ''
keywords:
  choices:
    - 'keywords="pipelines, machine learning, data pipelines, data science, data engineering",'
    - ''

_tasks:
  - 'pipx run black setup.py'
_answers_file: .setup-py-copier-answers.yml
```


## Results
``` yaml
# .setup-py-copier-answers.yml # Changes here will be overwritten by Copier; NEVER EDIT MANUALLY
_src_path: /home/walkers/.copier-templates/setup.py
author_github: waylonwalker
author_name: Waylon Walker
description: awesomeness
framework: null
keywords: null
package_name: my-package
```

## Update it
``` bash
copier -a .setup-py-copier-answers.yml update
```
## Stop asking all these damn questions
``` bash
copier -fa .setup-py-copier-answers.yml update
```
