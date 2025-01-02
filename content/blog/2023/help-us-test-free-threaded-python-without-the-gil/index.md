---
title: "Help us test free-threaded Python without the GIL"
date: "2024-05-10T12:18:27.904Z"
tags: ["python", "freethreaded", "testing", "cpython"]
---

Python 3.13 is [due out in October 2024](https://peps.python.org/pep-0719/) and work is
underway to implement _experimental support_ for
[PEP 703 - Making the Global Interpreter Lock Optional in CPython](https://peps.python.org/pep-0703/).

See also
[Free-threaded CPython](https://docs.python.org/3.13/whatsnew/3.13.html#free-threaded-cpython)
in "What's New in Python 3.13?"

As the Steering Council noted in their
[acceptance of the PEP](https://discuss.python.org/t/pep-703-making-the-global-interpreter-lock-optional-in-cpython-acceptance/37075?u=hugovk),
to succeed it's important to have community support.

Projects will need to test their code with free-threaded (aka "nogil" but
[don't call it that!](https://discuss.python.org/t/pep-703-making-the-global-interpreter-lock-optional-in-cpython-acceptance/37075?u=hugovk))
Python builds to help us find bugs in CPython, and to check their code is compatible.

Here's some ways to test.

- Official installers
- Build it yourself
- deadsnakes
- GitHub Actions?
- Fedora

## Official installers

The official macOS (starting in beta 2) and Windows installers has an option to install
the free-threading binaries, which also installs `python3.13t` alongside the regular
`python3.13`:

- [python/cpython#120098](https://github.com/python/cpython/issues/120098)
- https://docs.python.org/3.13/using/windows.html#installing-free-threaded-binaries

## Build it yourself

Check out the CPython Git repo and [build yourself](https://devguide.python.org/) using
the
[`--disable-gil` configuration flag](https://docs.python.org/3.13/using/configure.html#cmdoption-disable-gil).

For example, on macOS I run:

```console
$ GDBM_CFLAGS="-I$(brew --prefix gdbm)/include" \
  GDBM_LIBS="-L$(brew --prefix gdbm)/lib -lgdbm" \
  ./configure --config-cache \
              --with-system-libmpdec \
              --with-openssl="$(brew --prefix openssl@3.0)" \
              --disable-gil && make -s -j10
$ ./python.exe -c "import sysconfig; print(sysconfig.get_config_var('Py_GIL_DISABLED'))"
1
$ ./python.exe -c "import sys; print(sys._is_gil_enabled())"
False
```

More details in the devguide:

- https://devguide.python.org/getting-started/setup-building/

## GitHub Actions: deadsnakes/action

We can use the [deadsnakes/action](https://github.com/deadsnakes/action) to test Ubuntu.

For example:

```yaml
on: [push, pull_request, workflow_dispatch]

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.12, 3.13-dev]
    name: main
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        if: "!endsWith(matrix.python-version, '-dev')"
        with:
          python-version: ${{ matrix.python-version }}
      - uses: deadsnakes/action@v3.1.0
        if: endsWith(matrix.python-version, '-dev')
        with:
          python-version: ${{ matrix.python-version }}
          nogil: true
      - run: |
          python --version --version
          which python
          python -c "import sysconfig; print(sysconfig.get_config_var('Py_GIL_DISABLED'))"
          python -c "import sys; print(sys._is_gil_enabled())"
```

## GitHub Actions: actions/setup-python

I've asked for support at
[actions/setup-python#771](https://github.com/actions/setup-python/issues/771), they're
looking into it 🤞

In the meantime, give it an upvote, and use deadsnakes/action ⤴️

## deadsnakes: PPA

The deadsnakes project provides Personal Package Archives of Python packaged for Ubuntu,
included free-threaded builds.

For example, `python3.13-nogil` under `python3.13 - 3.13.0~a2-1+focal1` and
`python3.13 - 3.13.0~a2-1+jammy1` at
https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa/+packages

## Fedora

Fedora uses the `python3.13t` executable name
[as decided by the Steering Council](https://github.com/python/steering-council/issues/221#issuecomment-1841593283):

```console
$ # Install
$ sudo dnf install python3.13-freethreading
$ # Run
$ /usr/bin/python3.13t -c "import sysconfig; print(sysconfig.get_config_var('Py_GIL_DISABLED'))"
1
$ /usr/bin/python3.13t -c "import sys; print(sys._is_gil_enabled())"
False
```

## How to check your build

To confirm if you're using a free-threaded build, check the double `--version` option
(starting in beta 2):

```console
$ # Regular build
$ python3.13 --version --version
Python 3.13.0b2 (v3.13.0b2:3a83b172af, Jun  5 2024, 12:50:24) [Clang 15.0.0 (clang-1500.3.9.4)]
$ # Free-threaded build
$ python3.13t --version --version
Python 3.13.0b2 experimental free-threading build (v3.13.0b2:3a83b172af, Jun  5 2024, 12:57:31) [Clang 15.0.0 (clang-1500.3.9.4)]
```

Or the `Py_GIL_DISABLED` macro:

```console
$ # Regular build
$ python3.13 -c "import sysconfig; print(sysconfig.get_config_var('Py_GIL_DISABLED'))"
0
$ # Free-threaded build
$ python3.13t -c "import sysconfig; print(sysconfig.get_config_var('Py_GIL_DISABLED'))"
1
```

By default, the GIL is disabled for free-threaded builds, and can be re-enabled by
setting the `PYTHON_GIL` environment variable to `1` or running Python with `-X gil 1`.
You can check with `sys._is_gil_enabled()`:

```console
$ # Regular build: GIL is always enabled
$ python3.13 -c "import sys; print(sys._is_gil_enabled())"
True
$ # Free-threaded build: GIL is disabled by default
$ python3.13t -c "import sys; print(sys._is_gil_enabled())"
False
$ # Free-threaded build: re-enable with -X
$ python3.13t -X gil=1 -c "import sys; print(sys._is_gil_enabled())"
True
$ # Free-threaded build: re-enable with env var
$ PYTHON_GIL=1 python3.13t -c "import sys; print(sys._is_gil_enabled())"
True
```

References:

- https://docs.python.org/3.13/using/configure.html#cmdoption-disable-gil
- https://docs.python.org/3.13/using/cmdline.html#envvar-PYTHON_GIL
- https://docs.python.org/3.13/using/cmdline.html#cmdoption-X

## See also

- [Help test Python 3.13!](../../2024/help-test-python-313/)
- [C API Extension Support for Free Threading](https://docs.python.org/3.13/howto/free-threading-extensions.html)
- [Free-threaded CPython is ready to experiment with!](https://labs.quansight.org/blog/free-threaded-python-rollout)
- [py-free-threading](https://py-free-threading.github.io/)
- [Improving Ecosystem Compatibility with Free-Threaded Python](https://github.com/Quansight-Labs/free-threaded-compatibility)

---

<small>Header photo:
"<a target="_blank" rel="noopener noreferrer" href="https://www.flickr.com/photos/nlmhmd/8616809942/">George
Mayerle test chart</a>" by
<a target="_blank" rel="noopener noreferrer" href="https://www.flickr.com/people/nlmhmd/">US
National Library of Medicine</a>, with
<a target="_blank" rel="noopener noreferrer" href="https://www.flickr.com/commons/usage/">no
known copyright restrictions</a>.</small>
