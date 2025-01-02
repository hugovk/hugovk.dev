---
title: "The Python 3.1 problem"
date: "2021-05-19T14:08:31.844Z"
tags: ["yaml", "python", "testing", "ci"]
---

## Or, a variation on the Norway problem

Short version: put quotes around version numbers in YAML.

### The Norway problem

The [Norway problem](https://hitchdev.com/strictyaml/why/implicit-typing-removed/) is
when you put this in YAML:

```yaml
countries:
  - GB
  - IE
  - FR
  - DE
  - NO
```

But get this out:

```python
>>> import yaml
>>> with open("countries.yml") as f:
...     yaml.safe_load(f)
...
{'countries': ['GB', 'IE', 'FR', 'DE', False]}
```

:scream:

### The Norway fix

Use quotes:

```yaml
countries:
  - "GB"
  - "IE"
  - "FR"
  - "DE"
  - "NO"
```

```python
>>> with open("countries.yml") as f:
...     yaml.safe_load(f)
...
{'countries': ['GB', 'IE', 'FR', 'DE', 'NO']}
```

🇳🇴 ✅

### The Python 3.1 problem

A similar problem will affect the Python community in October 2021, when
[Python 3.10 comes out](https://peps.python.org/pep-0619/).

Why?

When `3.10` is added to YAML, for example in CI test matrix config, it's interpreted as
a float. This:

```yaml
python-version: [3.6, 3.7, 3.8, 3.9, 3.10, pypy3]
```

Turns into this:

```python
>>> import yaml
>>> with open("versions.yml") as f:
...     yaml.safe_load(f)
...
{'python-version': [3.6, 3.7, 3.8, 3.9, 3.1, 'pypy3']}
```

CI failed! It's not [2009](https://peps.python.org/pep-0375/)! Python 3.1 not found!

:scream:

Relatedly, `3.10-dev` without quotes works because it's interpreted as a string. But
when deleting `-dev`, `3.10` is interpreted as a float.

### The Python 3.10 fix

Version numbers are strings, not floats. Use quotes:

```yaml
python-version: ["3.6", "3.7", "3.8", "3.9", "3.10", "pypy3"]
```

```python
>>> import yaml
>>> with open("versions.yml") as f:
...     yaml.safe_load(f)
...
{'python-version': ['3.6', '3.7', '3.8', '3.9', '3.10', 'pypy3']}
```

🐍 ✅

### See also

[flake8-2020](https://github.com/asottile/flake8-2020/) is a useful Flake8 plugin to
find Python 3.10 and other bugs caused by assumptions about the length of version
numbers when using `sys.version` and `sys.version_info`.

---

<small>Header photo:
"<a target="_blank" rel="noopener noreferrer" href="https://www.flickr.com/photos/49968232@N00/2115403318">zero</a>"
by
<a target="_blank" rel="noopener noreferrer" href="https://www.flickr.com/photos/49968232@N00">Leo
Reynolds</a> is licensed under
<a target="_blank" rel="noopener noreferrer" href="https://creativecommons.org/licenses/by-nc-sa/2.0/?ref=openverse">CC
BY-NC-SA 2.0</a>.</small>
