---
title: "Help test Python 3.11 beta!"
date: "2022-05-31T17:10:00.000Z"
tags: ["python", "testing", "ci", "github-actions"]
---

Calling all Python library maintainers! 🐍

Python 3.11 is in beta! 🎉

[PEP 664](https://peps.python.org/pep-0664/#release-schedule) defines the release
schedule for Python 3.11.0:

- The second beta came out on 31st May 2022
- The first release candidate is set for 1st August 2022
- And the full release is set for 3rd October 2022

In his
[announcement](https://discuss.python.org/t/python-3-11-0b2-is-now-available/16111?u=hugovk),
Pablo Galindo Salgado, release manager for Python 3.10 and 3.11, said:

> We **strongly encourage** maintainers of third-party Python projects to **test with
> 3.11** during the beta phase and report issues found to the
> [Python bug tracker](https://github.com/python/cpython/issues) as soon as possible.
> While the release is planned to be feature complete entering the beta phase, it is
> possible that features may be modified or, in rare cases, deleted up until the start
> of the release candidate phase (Monday, 2021-08-02). Our goal is have no ABI changes
> after beta 4 and as few code changes as possible after 3.11.0rc1, the first release
> candidate. To achieve that, it will be **extremely important** to get as much exposure
> for 3.11 as possible during the beta phase.

## Test with 3.11

It's now time for library maintainers to start testing 3.11 with your project. You don't
need to declare support and release for 3.11 yet, but there's two big benefits to
testing with 3.11 on CI:

1. There have been removals and changes in Python 3.11. Testing now will help you make
   your code compatible and avoid any big surprises (for you and your users) at the big
   launch in October.

2. You might find bugs in Python itself! Reporting those will help get them fixed and
   help everyone.

## How

### GitHub Actions: setup-python

To test the latest alpha, beta or release candidate with
[actions/setup-python](https://github.com/actions/setup-python#available-versions-of-python),
add `3.11-dev` to your workflow matrix.

For example:

```yml
jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        python-version: ["3.7", "3.8", "3.9", "3.10", "3.11-dev"]

    steps:
      - uses: actions/checkout@v3

      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
```

### GitHub Actions: deadsnakes

For the bleeding edge, we can use
[deadsnakes/action](https://github.com/deadsnakes/action) to test the latest nightly
build:

```yml
jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        python-version: ["3.7", "3.8", "3.9", "3.10", "3.11-dev"]

    steps:
      - uses: actions/checkout@v3

      - name: Set up Python ${{ matrix.python-version }}
        if: "!endsWith(matrix.python-version, '-dev')"
        uses: actions/setup-python@v3
        with:
          python-version: ${{ matrix.python-version }}

      - uses: deadsnakes/action@v2.1.1
        name: Set up Python ${{ matrix.python-version }} (deadsnakes)
        if: endsWith(matrix.python-version, '-dev')
        with:
          python-version: ${{ matrix.python-version }}
```

### Travis CI

I recommend moving to another CI.

In the meantime, you can also add `3.11-dev` to `.travis.yml`, although at the time of
writing it's pointing to 3.11.0a3 from 2021-12-08, which is better than nothing.

```yml
language: python
python:
  - "3.7"
  - "3.8"
  - "3.9"
  - "3.10"
  - "3.11-dev"
```

Again, I recommend moving to another CI.

### Other CIs

Do you use other CIs? Please leave a comment if you know how to test 3.11!

## When to support 3.11?

When should you declare support and add the `Programming Language :: Python :: 3.11`
[Trove classifier](https://pypi.org/classifiers/)?

First of all, make sure your tests pass on 3.11 beta. One option is waiting until 3.11.0
final is released.

Or, as mentioned above:

> Our goal is have no ABI changes after beta 4 and as few code changes as possible after
> 3.11.0rc1, the first release candidate.

If you have a pure Python project, you could release now.

If you have C extensions, you might want to wait until the release candidate phase,
although if other projects depend on yours, a preview release would help them test and
prepare.

In any case, start testing 3.11 now!

---

<small>Header photo:
[Uppland Runic Inscription 53](https://en.wikipedia.org/wiki/Uppland_Runic_Inscription_53),
a 1,000 year old runestone in the old town of Stockholm
([source](https://www.flickr.com/photos/hugovk/3490246425/))</small>
