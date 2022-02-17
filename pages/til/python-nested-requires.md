---
date: 2022-02-17 15:53:20.138089
templateKey: til
title: Nested requirements.txt in python
tags:
  - python

---

python requirements text files can in fact depend on each other due to
the fact that you can pass pip install arguments right into your
`requirements.txt` file.  The trick is to just prefix the file with a
`-r` flag, just like you would if you were installing it with `pip
install`

## try it out
Lets create two requirements files in a new directory to play with.

``` bash
mkdir requirements-nest
cd requirements-nest
touch requirements.txt requirements_dev.txt
```

Then add the following to each requirements file.

``` txt
# requirements.txt
kedro[pandas.ParquetDataSet]
```

```txt
# requirements_dev.txt
-r requirements.txt
ipython
```

## Installing

Installing requirements_dev.txt will install both ipython and pandas
since it includes the base requirements file.

``` bash
# this will install only pandas
pip install -r requirements.txt

# this will install both ipython and pandas
pip install -r requirements_dev.txt
```

## Links

This is covered in the
[pip user guide](https://pip.pypa.io/en/stable/user_guide/),
but it is not obvious that this can be done in a requirements.txt
file.
