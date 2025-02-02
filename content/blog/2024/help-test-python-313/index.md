---
title: "Help test Python 3.13!"
date: "2024-06-04T13:04:03.640Z"
tags: ["python", "testing", "ci", "github-actions"]
---

Calling all Python library maintainers! 🐍

The Python 3.13 beta is out! 🎉

[PEP 719](https://peps.python.org/pep-0719/#release-schedule) defines the release
schedule for Python 3.13.0:

- The first beta candidate came out on 8th May 2024
- The first release candidate is set for 30th July 2024
- And the full release is set for 1st October 2024

In his
[announcement](https://discuss.python.org/t/python-3-13-0b1-now-available/52891?u=hugovk),
Thomas Wouters, release manager for Python 3.12 and 3.13, said:

> We **strongly encourage** maintainers of third-party Python projects to test with 3.13
> during the beta phase and report issues found to the
> [Python bug tracker](https://github.com/python/cpython/issues) as soon as possible.
> While the release is planned to be feature complete entering the beta phase, it is
> possible that features may be modified or, in rare cases, deleted up until the start
> of the release candidate phase (Tuesday 2024-07-30). Our goal is to have no ABI
> changes after beta 4 and as few code changes as possible after 3.13.0rc1, the first
> release candidate. To achieve that, it will be **extremely important** to get as much
> exposure for 3.13 as possible during the beta phase.

## Test with 3.13

It's now time for us library maintainers to start testing our projects with 3.13.
There's two big benefits:

1. There have been
   [removals and changes](https://docs.python.org/3.13/whatsnew/3.13.html#removed) in
   Python 3.13. Testing now helps us make our code compatible and avoid any big
   surprises (for us and our users) at the big launch in October.

2. We might find bugs in Python itself! Reporting those will help get them fixed and
   help everyone.

## How

### GitHub Actions: setup-python

To test the latest alpha, beta or release candidate with
[actions/setup-python](https://github.com/actions/setup-python#supported-version-syntax),
add `3.13` and `allow-prereleases: true` to your workflow matrix.

For example:

```yml
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        python-version: ["3.10", "3.11", "3.12", "3.13"]

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
          allow-prereleases: true
```

(We can instead use `3.13-dev` and omit `allow-prereleases: true`, but I find the above
a bit neater, and when 3.13.0 final is released in October, it will continue testing
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
        python-version: ["3.10", "3.11", "3.12", "3.13-dev"]

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python ${{ matrix.python-version }}
        if: "!endsWith(matrix.python-version, '-dev')"
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}

      - uses: deadsnakes/action@v3.1.0
        name: Set up Python ${{ matrix.python-version }} (deadsnakes)
        if: endsWith(matrix.python-version, '-dev')
        with:
          python-version: ${{ matrix.python-version }}
```

## When to support 3.13?

When should you declare support and add the `Programming Language :: Python :: 3.13`
[Trove classifier](https://pypi.org/classifiers/)? Some
[projects already have](https://pyreadiness.org/3.13/)!

If you have a pure Python project, you can release now.

If you have C extensions and other projects depend on yours, a preview release with
wheels will help them test and prepare. I've already started releasing these.

### ABI breaks?

ABI breaks during the beta are infrequent and unintentional. If they happen, you can
rebuild your wheels and upload them to an existing PyPI release by adding an optional
[_build tag_](https://packaging.python.org/en/latest/specifications/binary-distribution-format/#file-format)
to the filename:

> The wheel filename is
> `{distribution}-{version}(-{build tag})?-{python tag}-{abi tag}-{platform tag}.whl`.
>
> build tag: [...] Acts as a tie-breaker if two wheel file names are the same in all
> other respects (i.e. name, version, and other tags).

For example, this updates the filename and metadata with build number 1, and removes the
original file:

```sh
python -m pip install "wheel>=0.4.0"
wheel tags --build=1 --remove sampleproject-5.0.0-cp313-cp313-macosx_10_10_x86_64.whl
# this creates a file named sampleproject-5.0.0-1-cp313-cp313-macosx_10_10_x86_64.whl
```

Upload it, and the new file will be used instead of the old one. See also
[Brett Cannon's advice on making new wheels](https://snarky.ca/what-to-do-when-you-botch-a-release-on-pypi/#a-wheel-file-wasnt-compiled-properly).

In any case, let's start testing 3.13 now! 🚀

## See also

- [Help us test free-threaded Python without the GIL](../../2023/help-us-test-free-threaded-python-without-the-gil/)
- [What’s New In Python 3.13](https://docs.python.org/3.13/whatsnew/3.13.html)

---

<small>Header photo: Lot 044 from the [PyCon 2024](https://us.pycon.org/2024/)
[PyLadies Auction](https://mastodon.social/@Lorenanicole/112468770670490719): "A pair of
hand-woven snakes ([PyCon Latam](https://www.pylatam.org/) 2023 edition), donated by the
PyCon Latam Organizers. This is a souvenir from PyCon Latam held in Mexica 2023 that
represents the snakes of the PyLatam community logo. They are made completely by
hand."</small>
