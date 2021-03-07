---
templateKey: blog-post
related_post_label: Check out this related post
tags: []
title: python-deepwatch
date: 2020-04-27T05:00:00Z
status: published
description: ''
cover: ''

---
Is it possible to deep watch a single python function for changes?

## Shallow Watch

keeping track of a python functions hash is quite simple.  There is a`__hash__` method attached to every python function.  Calling it will return a hash of the function. If the function changes the hash will change.

``` python
[ins] In [1]: def test():
         ...:     return "hello"

[ins] In [2]: test.__hash__()
Out[2]: 8760526380347

[ins] In [3]: test.__hash__()
Out[3]: 8760526380347

[ins] In [4]: def test():
         ...:     return "hello world"

[ins] In [5]: test.__hash__()
Out[5]: 8760525617988

[ins] In [6]: def test():
         ...:     return "hello"

[ins] In [7]: test.__hash__()
Out[7]: 8760526380491
```

Using hashlib provides a consistent hash.

``` python
import inspect
import hashlib
def test():
	return "hello"

[ins] In [17]: m.update(inspect.getsource(test).encode())

[ins] In [18]: m
Out[18]: <sha256 HASH object @ 0x7f7b7b70fde0>

[ins] In [19]: m.hexdigest()
Out[19]: '1f2ff4c69eb69b545469686edd6f849136e104cd535785891586d90620328757'

[ins] In [20]: m.update(inspect.getsource(test).encode())

[ins] In [21]: m.hexdigest()
Out[21]: '93638f2c944f34a9069af9242657b7de556fcc63742f4c27c4c8deedeb976a5f'

[ins] In [22]: m = hashlib.sha256()

[ins] In [23]: m.update(inspect.getsource(test).encode())

[ins] In [24]: m.update(inspect.getsource(test).encode())

[ins] In [25]: m = hashlib.sha256()

[ins] In [26]: m.update(inspect.getsource(test).encode())

[ins] In [27]: m.hexdigest()
Out[27]: '1f2ff4c69eb69b545469686edd6f849136e104cd535785891586d90620328757'

[ins] In [28]: def test():
          ...:     return "hello world"

[ins] In [29]: m = hashlib.sha256()

[ins] In [30]: m.update(inspect.getsource(test).encode())

[ins] In [31]: m.hexdigest()
Out[31]: '121fa3a3f295d49d4609505bc5e96d8b6a8ed3b496e4f3dc6c0ead73bef4e3c7'

[ins] In [32]: def test():
          ...:     return "hello"

[ins] In [33]: m = hashlib.sha256()

[ins] In [34]: m.update(inspect.getsource(test).encode())

[ins] In [35]: m.hexdigest()
Out[35]: '1f2ff4c69eb69b545469686edd6f849136e104cd535785891586d90620328757'
```
Now we have a consistent way to hash function code.

## Deep hashing


### Find dependencies

setup a function in a module with a dependency
``` python
       │ File: one.py
───────┼────────────────────────────────
   1   │ def one():
   2   │     return 1
   3   │
   4   │ def two():
   5   │     return one() + one()
```

``` python
>>> import one
>>> one.one.__code__.co_names
()
>>> one.two.__code__.co_names
('one', )
```

## Create Generic module importer by filepath

``` python
import importlib
import importlib.util
import os

def _import(path: Path, directory: Path, verbose: bool = False):
    """dynamically imports module given a path"""
    cwd = os.getcwd()
    os.chdir(directory)
    name = path.name
    # path = str(path).replace(str(directory) + "/", "")
    path = _make_path_relative(path, directory)
    try:
        spec = importlib.util.spec_from_file_location(name, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    except (ModuleNotFoundError, ValueError):
        module = _use_importmodule(
            str(path).replace(os.sep, ".").replace(".py", ""), verbose=verbose
        )
    os.chdir(cwd)

    return module


def _use_importmodule(path: Path, verbose: bool = False):
    """
    relative imports do not work well with importlib.util.spec_from_file_location,
    and require a sys.path.append to be imported correctly.  For this reason
    importlib.import_module is the second option.
    """

    # Not sure if this is needed, but it was never hit in a test
    # if path[0] == ".":
    #     path = path[1:]

    sys.path.append(os.getcwd())
    mod = importlib.import_module(path)
    sys.path.pop()  # clean up path, do not permananatly change users path
    return mod

```

### get code of dependency

the inspect module can tell us the filename of our current module.

``` python
import inspect
module_path = inspect.getfile(one.one)
module = _import(module_path)
```

now we can hash the dependency

``` python
nested_function = eval(f'module.{one.two.__code__.co_names[0]}"
```
