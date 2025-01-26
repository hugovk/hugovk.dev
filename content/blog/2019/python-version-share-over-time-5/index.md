---
title: "Python version share over time, 5"
date: "2019-11-04T14:40:48.914Z"
tags: ["python", "pypi", "python2", "python3"]
thumbnail: "pypi.png"
---

## January 2016 — October 2019

To celebrate the release of
[Python 3.8.0](https://discuss.python.org/t/python-3-8-0-is-now-available/2478?u=hugovk)
on [14th October 2019](https://peps.python.org/pep-0569/), and with
[less than two months left for Python 2](https://python2woop.pw/), here’s some
statistics showing how much different Python versions have been used over nearly four
years.

Here’s the pip installs for all packages from the
[Python Package Index (PyPI)](https://pypi.org/), between January 2016 and October 2019:

![pypi](pypi.png)

### [pip](https://github.com/pypa/pip)

The package installer

![pip](https://user-images.githubusercontent.com/1324225/68128596-ab54ab80-ff20-11e9-96fa-867b403efc89.png)

### [six](https://github.com/benjaminp/six)

Python 2 and 3 compatibility library

![six](https://user-images.githubusercontent.com/1324225/68128614-b60f4080-ff20-11e9-92e3-892f29ecceea.png)

### [NumPy](https://github.com/numpy/numpy)

Scientific computing library

![numpy](https://user-images.githubusercontent.com/1324225/68128663-d0491e80-ff20-11e9-9442-0546e1a9843c.png)

### [pytest](https://github.com/pytest-dev/pytest)

Testing framework

![pytest](https://user-images.githubusercontent.com/1324225/68128691-e0f99480-ff20-11e9-9bd8-87e12318d149.png)

### [pandas](https://github.com/pandas-dev/pandas)

Data analysis toolkit

![pandas](https://user-images.githubusercontent.com/1324225/68142151-9cc5be80-ff37-11e9-93d9-72edd2e35e6b.png)

### [Coverage.py](https://github.com/nedbat/coveragepy)

Code coverage testing

![coverage](https://user-images.githubusercontent.com/1324225/68128715-ea82fc80-ff20-11e9-80a9-515c4b5265c2.png)

### [Pillow](https://github.com/python-pillow/Pillow)

Imaging library

![pillow](https://user-images.githubusercontent.com/1324225/68128908-49e10c80-ff21-11e9-977e-f25dfa13b2d4.png)

### [Django](https://github.com/python-pillow/Pillow)

Web framework

![django](https://user-images.githubusercontent.com/1324225/68128927-52394780-ff21-11e9-80d6-1dadf2525ebc.png)

### [Matplotlib](https://github.com/matplotlib/matplotlib)

2D plotting library

![matplotlib](https://user-images.githubusercontent.com/1324225/68128947-5b2a1900-ff21-11e9-9386-d366a030fe7c.png)

### [Flake8](https://gitlab.com/pycqa/flake8)

Linter

![flake8](https://user-images.githubusercontent.com/1324225/68128961-62e9bd80-ff21-11e9-8a45-001c7ae06c1d.png)

### [Pylint](https://github.com/PyCQA/pylint/)

Linter

![pylint](https://user-images.githubusercontent.com/1324225/68128981-6bda8f00-ff21-11e9-9a97-903892a47823.png)

### [pylast](https://github.com/pylast/pylast)

Interface to Last.fm

![pylast](https://user-images.githubusercontent.com/1324225/68128999-77c65100-ff21-11e9-9ac0-7f9c6071b07a.png)

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
- [Python version share over time,
  1]({{< ref "/blog/2018/python-version-share-over-time-1/" >}}) (January
  2016 — June 2018)
- [Python version share over time,
  2]({{< ref "/blog/2018/python-version-share-over-time-2/" >}}) (January
  2016 — October 2018)
- [Python version share over time, 3](../../2019/python-version-share-over-time-3/)
  (January 2016 — December 2018)
- [Python version share over time, 4](../../2019/python-version-share-over-time-4/)
  (January 2016 — March 2019)
- [PyPI Stats](https://pypistats.org/): See package download data for the past 180 days,
  without needing to sign up for BigQuery
- [pypistats](https://github.com/hugovk/pypistats): A command-line tool to access data
  from PyPI Stats
