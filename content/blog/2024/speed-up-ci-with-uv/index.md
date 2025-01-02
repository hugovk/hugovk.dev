---
title: "Speed up CI with uv ⚡"
date: "2024-11-02T13:11:22.255Z"
tags: ["python", "testing", "githubactions", "uv"]
---

We can use [uv](https://github.com/astral-sh/uv) to make linting and testing on GitHub
Actions around 1.5 times as fast.

## Linting

When using [pre-commit](https://pre-commit.com/) for linting:

```yml
name: Lint

on: [push, pull_request, workflow_dispatch]

env:
  FORCE_COLOR: 1

permissions:
  contents: read

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          persist-credentials: false
      - uses: actions/setup-python@v5
        with:
          python-version: "3.x"
          cache: pip
      - uses: pre-commit/action@v3.0.1
```

We can replace [pre-commit/action](https://github.com/pre-commit/action) with
[tox-dev/action-pre-commit-uv](https://github.com/tox-dev/action-pre-commit-uv):

```diff
       - uses: actions/setup-python@v5
         with:
           python-version: "3.x"
-          cache: pip
-      - uses: pre-commit/action@v3.0.1
+      - uses: tox-dev/action-pre-commit-uv@v1
```

```yml
name: Lint

on: [push, pull_request, workflow_dispatch]

env:
  FORCE_COLOR: 1

permissions:
  contents: read

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          persist-credentials: false
      - uses: actions/setup-python@v5
        with:
          python-version: "3.x"
      - uses: tox-dev/action-pre-commit-uv@v1
```

This means uv will create virtual environments and install packages for pre-commit,
which is faster for the initial seed operation when there's no cache.

### Lint comparison

For example: [python/blurb#32](https://github.com/python/blurb/pull/32)

|                | Before                                                                          | After                                                                           | Times faster |
| -------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------ |
| **No cache**   | [60s](https://github.com/hugovk/blurb/actions/runs/11635610765/job/32405339441) | [37s](https://github.com/hugovk/blurb/actions/runs/11635612034/job/32405343101) | 1.62         |
| **With cache** | [11s](https://github.com/hugovk/blurb/actions/runs/11635702058/job/32405618322) | [11s](https://github.com/hugovk/blurb/actions/runs/11635703339/job/32405622146) | 1.00         |

## Testing

When testing with tox:

```yml
name: Test

on: [push, pull_request, workflow_dispatch]

permissions:
  contents: read

env:
  FORCE_COLOR: 1

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        python-version: ["3.9", "3.10", "3.11", "3.12", "3.13", "3.14"]

    steps:
      - uses: actions/checkout@v4
        with:
          persist-credentials: false

      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
          allow-prereleases: true
          cache: pip

      - name: Install dependencies
        run: |
          python --version
          python -m pip install -U pip
          python -m pip install -U tox

      - name: Tox tests
        run: |
          tox -e py
```

We can replace [tox](https://github.com/tox-dev/tox) with
[tox-uv](https://github.com/tox-dev/tox-uv):

```diff
       - name: Set up Python ${{ matrix.python-version }}
         uses: actions/setup-python@v5
         with:
           python-version: ${{ matrix.python-version }}
           allow-prereleases: true
-          cache: pip

-      - name: Install dependencies
-        run: |
-          python --version
-          python -m pip install -U pip
-          python -m pip install -U tox
+      - name: Install uv
+        uses: hynek/setup-cached-uv@v2

       - name: Tox tests
         run: |
-          tox -e py
+          uvx --with tox-uv tox -e py
```

```yml
name: Test

on: [push, pull_request, workflow_dispatch]

permissions:
  contents: read

env:
  FORCE_COLOR: 1

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        python-version: ["3.9", "3.10", "3.11", "3.12", "3.13"]

    steps:
      - uses: actions/checkout@v4
        with:
          persist-credentials: false

      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
          allow-prereleases: true

      - name: Install uv
        uses: hynek/setup-cached-uv@v2

      - name: Tox tests
        run: |
          uvx --with tox-uv tox -e py
```

tox-uv is tox plugin to replace virtualenv and pip with uv in your tox environments. We
only need to install uv, and use `uvx` to both install tox-uv and run tox, for faster
installs of tox, the virtual environment, and the dependencies within it.

### Test comparison

For example: [python/blurb#32](https://github.com/python/blurb/pull/32)

|                | Before                                                                   | After                                                                    | Times faster |
| -------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------ |
| **No cache**   | [2m 0s](https://github.com/hugovk/blurb/actions/runs/11635722298/usage)  | [1m 26s](https://github.com/hugovk/blurb/actions/runs/11635723255/usage) | 1.40         |
| **With cache** | [1m 58s](https://github.com/hugovk/blurb/actions/runs/11635745236/usage) | [1m 22s](https://github.com/hugovk/blurb/actions/runs/11635746618/usage) | 1.44         |

### No pip with tox-uv

One difference with uv environments compared to regular venv/virtualenv ones is that
they do not have pip. This means calls to pip need replacing, for example in `tox.ini`:

```diff
 [testenv]
-commands_pre =
-    {envpython} -m pip install -U -r requirements.txt
+deps =
+    -r requirements.txt
 pass_env =
     FORCE_COLOR
 commands =
     {envpython} -m pytest {posargs}
```

If you still need pip (or setuptools or wheel), add
[`uv_seed = True`](https://github.com/tox-dev/tox-uv#environment-creation) to your
`[testenv]` to inject them.

## Bonus tip

Run the new tool [zizmor](https://github.com/woodruffw/zizmor) to find security issues
in GitHub Actions.

---

<small>Header photo:
"<a target="_blank" rel="noopener noreferrer" href="https://finna.fi/Record/hkm.BB327C7B-90B8-45DF-90A1-ABC7B74F6BAA?imgid=1">Road
cycling at the 1952 Helsinki Olympics</a>" by
<a target="_blank" rel="noopener noreferrer" href="https://www.flickr.com/people/nlmhmd/">Olympia-Kuva
Oy & Helsinki City Museum</a>,
<a target="_blank" rel="noopener noreferrer" href="https://creativecommons.org/publicdomain/mark/1.0/deed.en">Public
Domain</a>.</small>
