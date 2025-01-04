---
title: "Python version share over time, 4"
date: "2019-04-04T14:58:18.829Z"
tags: ["python", "pypi", "python2", "python3", "statistics"]
---

## January 2016 — March 2019

To celebrate the release of
[Python 3.7.3](https://www.python.org/downloads/release/python-373/) on
[25th March 2019](https://peps.python.org/pep-0537/), and with under
[nine months left for Python 2](https://python2woop.pw/), here’s some statistics showing
how much different Python versions have been used over the past three years.

Here’s the pip installs for all packages from the
[Python Package Index (PyPI)](https://pypi.org/), between January 2016 and March 2019:

![pypi](4wqa702ngppsv6dxh3zq.png)

### [pip](https://github.com/pypa/pip)

The package installer

![pip](2kncm0d1gnytc8dox1vr.png)

### [six](https://github.com/benjaminp/six)

Python 2 and 3 compatibility library

![six](2s8ienw3purly7d563g3.png)

### [NumPy](https://github.com/numpy/numpy)

Scientific computing library

![NumPy](slcl0es81ltkdlduthea.png)

### [pytest](https://github.com/pytest-dev/pytest)

Testing framework

![pytest](x9u45cebj930u52lhob2.png)

### [Coverage.py](https://github.com/nedbat/coveragepy)

Code coverage testing

![coverage](lacortkwvi92z4zw0m6b.png)

### [Pillow](https://github.com/python-pillow/Pillow)

Imaging library

![pillow](msqm643wek2w0qmgdxlu.png)

### [Django](https://github.com/python-pillow/Pillow)

Web framework

![django](omjea829j1h83fxp65ge.png)

### [Matplotlib](https://github.com/matplotlib/matplotlib)

2D plotting library

![matplotlib](7kqrb64d2lmrnm2jw2lu.png)

### [Flake8](https://gitlab.com/pycqa/flake8)

Linter

![flake8](102lu27lpme6gtdb3q9i.png)

### [Pylint](https://github.com/PyCQA/pylint/)

Linter

![pylint](yxc1911cdltvfrjs0eop.png)

### [pylast](https://github.com/pylast/pylast)

Interface to Last.fm

![pylast](ulztdisgv3zmuzif8nbf.png)

## How

Statistics were collected using
[pypi-trends.py](https://github.com/hugovk/pypi-tools/blob/master/pypi-trends.py), a
wrapper around [pypinfo](https://github.com/ofek/pypinfo) to fetch all monthly downloads
from the PyPI database on Google BigQuery and save them as JSON files. Data was
downloaded over several days as getting all months uses up a lot of free BigQuery quota.
Then [jsons2csv.py](https://github.com/hugovk/pypi-tools/blob/master/jsons2csv.py) plots
a chart using [matplotlib](https://github.com/matplotlib/matplotlib). Raw JSON data is
in the [repo](https://github.com/hugovk/pypi-tools/tree/master/data).

## See also

- [Data Driven Decisions Using PyPI Download Statistics](https://langui.sh/2016/12/09/data-driven-decisions/)
- [Python version share over time,
  1]({{< ref "/blog/2018/python-version-share-over-time-1/" >}}) (January
  2016 — June 2018)
- [Python version share over time,
  2]({{< ref "/blog/2018/python-version-share-over-time-2/" >}}) (January
  2016 — October 2018)
- [Python version share over time, 3](../../2019/python-version-share-over-time-3/)
  (January 2016 — December 2018)
- [PyPI Stats](https://pypistats.org/): See package download data for the past 180 days,
  without needing to sign up for BigQuery
- [pypistats](https://github.com/hugovk/pypistats): A command-line tool to access data
  from PyPI Stats
