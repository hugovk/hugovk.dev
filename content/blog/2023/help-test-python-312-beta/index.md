---
title: "Help test the Python 3.12 release candidate!"
date: "2023-05-26T12:30:43.172Z"
tags: ["python", "testing", "ci", "githubactions"]
---

Calling all Python library maintainers! 🐍

The _third and final_ Python 3.12 release candidate is out! 🎉

[PEP 693](https://peps.python.org/pep-0693/#release-schedule) defines the release
schedule for Python 3.12.0:

- The first release candidate came out on 6th August 2023
- The second ~~and final~~ release candidate came out on 6th September 2023
- The third and final release candidate came out on 19th September 2023
- And the full release is set for **2nd October 2023**

In his
[announcement](https://discuss.python.org/t/python-3-12-0rc3-released-honestly-the-final-release-candidate-i-swear/34093?u=hugovk),
Thomas Wouters, release manager for Python 3.12 and 3.13, said:

> We strongly encourage maintainers of third-party Python projects to prepare their
> projects for 3.12 compatibilities during this phase, and where necessary publish
> Python 3.12 wheels on PyPI to be ready for the final release of 3.12.0. Any binary
> wheels built against Python 3.12.0rc3 will work with future versions of Python 3.12.
> As always, report any issues to
> [the Python bug tracker](https://github.com/python/cpython/issues).

## Test with 3.12

It's now time for us library maintainers to start testing our projects with 3.12.
There's two big benefits:

1. There have been
   [removals and changes](https://docs.python.org/3.12/whatsnew/3.12.html#removed) in
   Python 3.12. Testing now helps us make our code compatible and avoid any big
   surprises (for us and our users) at the big launch in October.

2. We might find bugs in Python itself! Reporting those will help get them fixed and
   help everyone.

## How

### GitHub Actions: setup-python

To test the latest alpha, beta or release candidate with
[actions/setup-python](https://github.com/actions/setup-python#supported-version-syntax),
add `3.12` and `allow-prereleases: true` to your workflow matrix.

For example:

```yml
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        python-version: ["3.8", "3.9", "3.10", "3.11", "3.12"]

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
          allow-prereleases: true
```

(We can instead use `3.12-dev` and omit `allow-prereleases: true`, but I find the above
a bit neater, and when 3.12.0 final is released in October, it will continue testing
with full release versions.)

### GitHub Actions: deadsnakes

For the bleeding edge, we can use
[deadsnakes/action](https://github.com/deadsnakes/action) to test the latest nightly
build:

```yml
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        python-version: ["3.8", "3.9", "3.10", "3.11", "3.12-dev"]

    steps:
      - uses: actions/checkout@v3

      - name: Set up Python ${{ matrix.python-version }}
        if: "!endsWith(matrix.python-version, '-dev')"
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}

      - uses: deadsnakes/action@v3.0.0
        name: Set up Python ${{ matrix.python-version }} (deadsnakes)
        if: endsWith(matrix.python-version, '-dev')
        with:
          python-version: ${{ matrix.python-version }}
```

### Travis CI

I recommend moving to another CI.

In the meantime, you can also add `3.12-dev` to `.travis.yml`, although at the time of
writing it's pointing to 3.12.0a3+ from 2022-12-07, which is better than nothing.

```yml
language: python
python:
  - "3.8"
  - "3.9"
  - "3.10"
  - "3.11"
  - "3.12-dev"
```

Again, I recommend moving to another CI.

### Other CIs

Do you use other CIs? Please leave a comment if you know how to test 3.12!

## When to support 3.12?

Now is also a good time to declare support and add the
`Programming Language :: Python :: 3.12`
[Trove classifier](https://pypi.org/classifiers/).

Especially if you have C extensions and other projects depend on yours, a release with
wheels will help them test and prepare.

### ABI breaks?

From the announcement:

> There will be **no ABI changes** from this point forward in the 3.12 series. The
> intent is for the final release of 3.12.0, scheduled for Monday, 2023-10-02, to be
> identical to this release candidate. **This really is the last chance to find critical
> problems in Python 3.12.**

Let's start testing and releasing for 3.12 now! 🚀

---

<small>Header photo: The carpet of the Salt Palace Convention Center grand ballroom,
host of [PyCon 2023](https://us.pycon.org/2023/), with a couple of googly eyes added to
make them Pythony ([source](https://mastodon.social/@hugovk/110239504743679454))</small>

<small>2023-08-14: Updated for RC1</small> <small>2023-09-06: Updated for RC2</small>
<small>2023-09-19: Updated for RC3</small>
