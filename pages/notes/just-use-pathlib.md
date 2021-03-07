---
templateKey: blog-post
related_post_label: Check out this related post
tags:
- python
title: Just Use Pathlib
date: 2019-09-26T05:00:00.000+00:00
status: published
description: Pathlib is an amazing cross-platform path tool.
cover: ''

---
Pathlib is an amazing cross-platform path tool.

## Import

```python
from pathlib import Path
```

## Create path object

**Current Directory**

```python
cwd = Path('.').absolute()
```

**Users Home Directory**

```python
home = Path.home()
```

**module directory**

```python
module_path = Path(__file__)
```

**Others**
Let's create a path relative to our current module.

```python
data_path = Path(__file__) / 'data'
```

## Check if files exist

## Make Directories

```python
data_path.mkdir(parents=True, exists_ok=True)
```

## rename files

```python
Path(data_path /'example.csv').rename('real.csv')
```

## List files

## Glob Files

```python
data_path.glob('*.csv')
```

**recursively**

```python
data_path.rglob('*.csv')
```

## Write

```python
Path(data_path / 'meta.txt').write_text(f'created on {datetime.datetime.today()})
```
