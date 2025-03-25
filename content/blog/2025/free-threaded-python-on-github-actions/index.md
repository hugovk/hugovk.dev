---
title: "Free-threaded Python on GitHub Actions"
date: "2025-03-25T10:25:00Z"
tags: ["python", "free-threaded", "testing", "cpython", "CI", "github-actions"]
featureAlt:
  "View of the spinning room of a wool cloth manufacturing factory on Broad Street in
  Philadelphia, late nineteenth-century. Shows two women operating machines that wind
  bobbins with woolen thread for weaving."
---

GitHub Actions now supports _experimental_ free-threaded CPython!

There are three ways to add it to your test matrix:

- actions/setup-python: `t` suffix
- actions/setup-uv: `t` suffix
- actions/setup-python: `freethreaded` variable

## actions/setup-python: `t` suffix

Using [actions/setup-python](https://github.com/actions/setup-python#basic-usage), you
can add the `t` suffix for Python versions 3.13 and higher: `3.13t` and `3.14t`.

This is my preferred method, we can clearly see which versions are free-threaded and
it's straightforward to test both regular and free-threaded builds.

```yml
on: [push, pull_request, workflow_dispatch]

jobs:
  build:
    runs-on: ${{ matrix.os }}
    strategy:
      fail-fast: false
      matrix:
        python-version: [
            "3.13",
            "3.13t", # add this!
            "3.14",
            "3.14t", # add this!
          ]
        os: ["windows-latest", "macos-latest", "ubuntu-latest"]

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
          allow-prereleases: true # needed for 3.14

      - run: |
          python --version --version
          python -c "import sys; print('sys._is_gil_enabled:', sys._is_gil_enabled())"
          python -c "import sysconfig; print('Py_GIL_DISABLED:', sysconfig.get_config_var('Py_GIL_DISABLED'))"
```

Regular builds will output something like:

```
Python 3.14.0a6 (main, Mar 17 2025, 02:44:29) [GCC 13.3.0]
sys._is_gil_enabled: True
Py_GIL_DISABLED: 0
```

And free-threaded builds will output something like:

```
Python 3.14.0a6 experimental free-threading build (main, Mar 17 2025, 02:44:30) [GCC 13.3.0]
sys._is_gil_enabled: False
Py_GIL_DISABLED: 1
```

For example:
[hugovk/test/actions/runs/14057185035](https://github.com/hugovk/test/actions/runs/14057185035)

## actions/setup-uv: `t` suffix

Similarly, you can install uv with
[astral/setup-uv](https://github.com/astral-sh/setup-uv#python-version) and use that to
set up free-threaded Python using the `t` suffix.

```yml
on: [push, pull_request, workflow_dispatch]

jobs:
  build:
    runs-on: ${{ matrix.os }}
    strategy:
      fail-fast: false
      matrix:
        python-version: [
            "3.13",
            "3.13t", # add this!
            "3.14",
            "3.14t", # add this!
          ]
        os: ["windows-latest", "macos-latest", "ubuntu-latest"]

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python ${{ matrix.python-version }}
        uses: astral-sh/setup-uv@v5 # change this!
        with:
          python-version: ${{ matrix.python-version }}
          enable-cache: false # only needed for this example with no dependencies

      - run: |
          python --version --version
          python -c "import sys; print('sys._is_gil_enabled:', sys._is_gil_enabled())"
          python -c "import sysconfig; print('Py_GIL_DISABLED:', sysconfig.get_config_var('Py_GIL_DISABLED'))"
```

For example:
[hugovk/test/actions/runs/13967959519](https://github.com/hugovk/test/actions/runs/13967959519)

## actions/setup-python: `freethreaded` variable

Back to actions/setup-python, you can also set the `freethreaded` variable for `3.13`
and higher.

```yml
on: [push, pull_request, workflow_dispatch]

jobs:
  build:
    runs-on: ${{ matrix.os }}
    strategy:
      fail-fast: false
      matrix:
        python-version: ["3.13", "3.14"]
        os: ["windows-latest", "macos-latest", "ubuntu-latest"]

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
          allow-prereleases: true # needed for 3.14
          freethreaded: true # add this!

      - run: |
          python --version --version
          python -c "import sys; print('sys._is_gil_enabled:', sys._is_gil_enabled())"
          python -c "import sysconfig; print('Py_GIL_DISABLED:', sysconfig.get_config_var('Py_GIL_DISABLED'))"
```

For example:
[hugovk/test/actions/runs/39359291708](https://github.com/hugovk/test/actions/runs/39359291708)

## `PYTHON_GIL=0`

And you may want to set `PYTHON_GIL=0` to force Python to keep the GIL disabled, even
after importing a module that doesn't support running without it.

See
[Running Python with the GIL Disabled](https://py-free-threading.github.io/running-gil-disabled/)
for more info.

With the `t` suffix:

```yml
- name: Set PYTHON_GIL
  if: endsWith(matrix.python-version, 't')
  run: |
    echo "PYTHON_GIL=0" >> "$GITHUB_ENV"
```

With the `freethreaded` variable:

```yml
- name: Set PYTHON_GIL
  if: "${{ matrix.freethreaded }}"
  run: |
    echo "PYTHON_GIL=0" >> "$GITHUB_ENV"
```

## Please test!

For free-threaded Python to succeed and become the default, it's essential there is
ecosystem and community support. Library maintainers: please test it and where needed,
adapt your code, and publish
[free-threaded wheels](https://hugovk.github.io/free-threaded-wheels/) so others can
test _their_ code that depends on _yours_. Everyone else: please test your code too!

## See also

- [Help us test free-threaded Python without the GIL](../../2023/help-us-test-free-threaded-python-without-the-gil/)
  for other ways to test and how to check your build
- [Python free-threading guide](https://py-free-threading.github.io/)
- [actions/setup-python#973](https://github.com/actions/setup-python/pull/973)
- [actions/setup-python@v5.5.0](https://github.com/actions/setup-python/releases/tag/v5.5.0)

---

<small>Header photo:
"<a target="_blank" rel="noopener noreferrer" href="https://www.flickr.com/photos/library-company-of-philadelphia/9354604392/">Spinning
Room, Winding Bobbins with Woolen Yarn for Weaving, Philadelphia, PA</a>" by
<a target="_blank" rel="noopener noreferrer" href="https://www.flickr.com/photos/library-company-of-philadelphia/">Library
Company of Philadelphia</a>, with
<a target="_blank" rel="noopener noreferrer" href="https://www.flickr.com/commons/usage/">no
known copyright restrictions</a>.</small>
