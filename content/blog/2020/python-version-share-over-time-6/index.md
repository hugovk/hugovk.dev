---
title: "Python version share over time, 6"
date: "2020-01-01T16:36:25.878Z"
tags: ["python", "pypi", "python2", "python3", "statistics"]
---

## January 2016 — December 2019

To celebrate the end of life of [Python 2](https://www.python.org/doc/sunset-python-2/)
on [1st January 2020](https://peps.python.org/pep-0373/), here’s some statistics showing
how much different Python versions have been used over four years.

Here’s the pip installs for all packages from the
[Python Package Index (PyPI)](https://pypi.org/), between January 2016 and December
2019:

![all](https://user-images.githubusercontent.com/1324225/71643621-a748ce00-2cc4-11ea-9dc7-a6dd57ce9a66.png)

### [pip](https://github.com/pypa/pip)

The package installer

![pip](https://user-images.githubusercontent.com/1324225/71643625-af087280-2cc4-11ea-9997-10aae072ac1d.png)

### [six](https://github.com/benjaminp/six)

Python 2 and 3 compatibility library

![six](https://user-images.githubusercontent.com/1324225/71643630-b62f8080-2cc4-11ea-9461-1204f4dd117e.png)

### [NumPy](https://github.com/numpy/numpy)

Scientific computing library

![numpy](https://user-images.githubusercontent.com/1324225/71643635-bb8ccb00-2cc4-11ea-9c4f-7095b15210f6.png)

### [pytest](https://github.com/pytest-dev/pytest)

Testing framework

![pytest](https://user-images.githubusercontent.com/1324225/71643639-c0ea1580-2cc4-11ea-9aef-2a0d9cf816ae.png)

### [pandas](https://github.com/pandas-dev/pandas)

Data analysis toolkit

![pandas](https://user-images.githubusercontent.com/1324225/71643641-c8a9ba00-2cc4-11ea-8f58-9c244ff958aa.png)

### [Coverage.py](https://github.com/nedbat/coveragepy)

Code coverage testing

![coverage](https://user-images.githubusercontent.com/1324225/71643645-ce070480-2cc4-11ea-85b5-e408ea682e31.png)

### [Pillow](https://github.com/python-pillow/Pillow)

Imaging library

![pillow](https://user-images.githubusercontent.com/1324225/71643648-d3644f00-2cc4-11ea-9b3e-7271788d1f5d.png)

### [Django](https://github.com/python-pillow/Pillow)

Web framework

![django](https://user-images.githubusercontent.com/1324225/71643651-d95a3000-2cc4-11ea-891e-a218090c5db9.png)

### [Matplotlib](https://github.com/matplotlib/matplotlib)

2D plotting library

![matplotlib](https://user-images.githubusercontent.com/1324225/71643656-e6771f00-2cc4-11ea-808a-464ee01f88b5.png)

### [Flake8](https://gitlab.com/pycqa/flake8)

Linter

![flake8](https://user-images.githubusercontent.com/1324225/71643661-ec6d0000-2cc4-11ea-9ef8-f5da11826684.png)

### [Pylint](https://github.com/PyCQA/pylint/)

Linter

![pylint](https://user-images.githubusercontent.com/1324225/71643663-f42ca480-2cc4-11ea-9588-7290df0fa003.png)

### [TensorFlow](https://github.com/tensorflow/tensorflow/)

Machine learning library

![tensorflow](https://user-images.githubusercontent.com/1324225/71645996-1506f100-2ce9-11ea-80d8-43b499348a54.png)

### [pylast](https://github.com/pylast/pylast)

Interface to Last.fm

![pylast](https://user-images.githubusercontent.com/1324225/71643665-f989ef00-2cc4-11ea-921e-1d705524151c.png)

## How

Statistics were collected using
[pypi-trends.py](https://github.com/hugovk/pypi-tools/blob/master/pypi-trends.py), a
wrapper around [pypinfo](https://github.com/ofek/pypinfo) and
[pypistats](https://github.com/hugovk/pypistats) to fetch all monthly downloads from the
PyPI database on Google BigQuery and save them as JSON files. Data was downloaded over
several days as getting all months uses up a lot of free BigQuery quota. Then
[jsons2csv.py](https://github.com/hugovk/pypi-tools/blob/master/jsons2csv.py) plots a
chart using [matplotlib](https://github.com/matplotlib/matplotlib). Raw JSON data is in
the [repo](https://github.com/hugovk/pypi-tools/tree/master/data).

## See also

- [Data Driven Decisions Using PyPI Download Statistics](https://langui.sh/2016/12/09/data-driven-decisions/)
- [Python version share over time, 1](../../2018/python-version-share-over-time-1/)
  (January 2016 — June 2018)
- [Python version share over time, 2](../../2018/python-version-share-over-time-2/)
  (January 2016 — October 2018)
- [Python version share over time, 3](../../2019/python-version-share-over-time-3/)
  (January 2016 — December 2018)
- [Python version share over time, 4](../../2019/python-version-share-over-time-4/)
  (January 2016 — March 2019)
- [Python version share over time, 5](../../2019/python-version-share-over-time-5/)
  (January 2016 — October 2019)
- [PyPI Stats](https://pypistats.org/): See package download data for the past 180 days,
  without needing to sign up for BigQuery
- [pypistats](https://github.com/hugovk/pypistats): A command-line tool to access data
  from PyPI Stats
