---
title: "Python version share over time, 3"
date: "2019-01-01T14:40:48.914Z"
tags: ["python", "pypi", "python2", "python3", "statistics"]
---

## January 2016 — December 2018

To celebrate the release of
[Python 3.7.2](https://www.python.org/downloads/release/python-372/) on
[Christmas Eve 2018](https://peps.python.org/pep-0537/), and with
u[nder a year left for Python 2](https://hugovk.github.io/python2-progress-bar/), here's
some statistics showing how much different Python versions have been used over the past
three years.

Here's the pip installs for all packages from the
[Python Package Index (PyPI)](https://pypi.org/), between January 2016 and December
2018:

![pypi](pypi.png)

For the [NumPy](https://github.com/numpy/numpy) scientific computing library:

![NumPy](numpy.png)

For the [pytest](https://github.com/pytest-dev/pytest) testing framework:

![pytest](pytest.png)

For the [Pillow](https://github.com/python-pillow/Pillow) imaging library:

![pillow](pillow.png)

For the [Django](https://github.com/django/django) web framework:

![django](django.png)

For the [matplotlib](https://github.com/matplotlib/matplotlib) 2D plotting library:

![matplotlib](matplotlib.png)

For the [Pylint](https://github.com/PyCQA/pylint) linter:

![pylint](pylint.png)

And for the [pylast](https://github.com/pylast/pylast) interface to Last.fm:

![pylast](pylast.png)

## How

Statistics were collected using
[pypi-trends.py](https://github.com/hugovk/pypi-tools/blob/master/pypi-trends.py) a
wrapper around [pypinfo](https://github.com/ofek/pypinfo) to fetch all monthly downloads
from the PyPI database on Google BigQuery and save them as JSON files. Data was
downloaded over several days as getting all months uses up a lot of free BigQuery quota.
Then [jsons2csv.py](https://github.com/hugovk/pypi-tools/blob/master/jsons2csv.py) plots
a chart using [matplotlib](https://github.com/matplotlib/matplotlib). Raw JSON data is
in the [repo](https://github.com/hugovk/pypi-tools/tree/master/data).

## See also

- [Data Driven Decisions Using PyPI Download Statistics](https://langui.sh/2016/12/09/data-driven-decisions/)
- [Python version share over time, 1](../../2018/python-version-share-over-time-1/)
  (January 2016 — June 2018)
- [Python version share over time, 2](../../2018/python-version-share-over-time-2/)
  (January 2016 — October 2018)
- [PyPI Stats](https://pypistats.org/): See package download data for the past 180 days,
  without needing to sign up for BigQuery
- [pypistats](https://github.com/hugovk/pypistats): A command-line tool to access data
  from PyPI Stats
