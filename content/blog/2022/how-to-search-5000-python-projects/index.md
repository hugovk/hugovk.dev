---
title: "How to search 5,000 Python projects"
date: "2022-12-09T12:44:21.510Z"
tags: ["python", "search", "pypi", "deprecation"]
---

## Why?

Often Python core developers think about deprecating and removing old bits of the
language. But first it's a good idea to get an idea of how much the old bits are used.
Searching the
[5,000 most-popular projects on PyPI](https://hugovk.github.io/top-pypi-packages/) is a
helpful proxy to gauge community use.

## How?

Core developer [Victor Stinner](https://vstinner.readthedocs.io/) has written a couple
of useful scripts that live in his [misc](https://github.com/vstinner/misc) repo.

## Setup

First, clone the repo somewhere, doesn't matter where:

```sh
mkdir -p ~/github
cd ~/github/
git clone https://github.com/vstinner/misc

# Optionally for some colour in the logs:
python3 -m pip install termcolor
```

Then download 5,000 sdists! Again, doesn't matter where:

```console
$ mkdir -p ~/top-pypi/output
$ cd ~/top-pypi/output/
$ python3 ~/github/misc/cpython/download_pypi_top.py .
Download JSON from: https://hugovk.github.io/top-pypi-packages/top-pypi-packages-30-days.min.json
Project#: 5000
[1/5000] Saving to ./boto3-1.26.25.tar.gz (101.7 kB)
[2/5000] Saving to ./botocore-1.29.25.tar.gz (10426.8 kB)
[3/5000] Saving to ./urllib3-1.26.13.tar.gz (293.4 kB)
...
[4990/5000] Saving to ./meld3-2.0.1.tar.gz (35.3 kB)
[4991/5000] Saving to ./browserstack-local-1.2.4.tar.gz (6.6 kB)
Cannot find URL for project: allensdk
Cannot find URL for project: dataframe-image
[4994/5000] Saving to ./SQLAlchemy-Continuum-1.3.13.tar.gz (79.2 kB)
[4995/5000] Saving to ./sarge-0.1.7.post1.tar.gz (25.1 kB)
[4996/5000] Saving to ./confusable_homoglyphs-3.2.0.tar.gz (158.1 kB)
[4997/5000] Saving to ./YTThumb-1.4.5.tar.gz (3.0 kB)
[4998/5000] Saving to ./azure-ai-ml-1.2.0.zip (4486.3 kB)
[4999/5000] Saving to ./pythena-1.6.0.tar.gz (5.2 kB)
[5000/5000] Saving to ./interchange-2021.0.4.tar.gz (25.2 kB)
Downloaded 5000 projects in 1602.4 seconds
```

With colour:

![Tail end of downloading files: successful downloads in green, unsuccessful downloads in red](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/v41t4zfbxoybdfxuhg6m.png)

⏳ This will take a bit of time. Some projects don't have sdists, nothing to worry
about, we will still end up with a good number. At the time of writing (2022-12-09), it
took me just under 27 minutes to download 4,748 files, taking up 5.37 GB of space.

If you want to download fewer, specify how many:

```sh
python3 ~/github/misc/cpython/download_pypi_top.py . 100
```

## Search

Next, we can search all the sdists using another script. And we don't need to extract
them!

For example, `configparser`'s `LegacyInterpolation` was deprecated in
[Python 3.2](https://peps.python.org/pep-0392/) (released February 2011), but only in
docs and without raising a
[`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning).

How much is it used in the top 5k?

```console
$ cd ~/top-pypi/output/
$ python3 ~/github/misc/cpython/search_pypi_top.py -q . "LegacyInterpolation"
./hexbytes-0.3.0.tar.gz: hexbytes-0.3.0/.tox/lint/lib/python3.9/site-packages/mypy/typeshed/stdlib/configparser.pyi: "LegacyInterpolation",
./hexbytes-0.3.0.tar.gz: hexbytes-0.3.0/.tox/lint/lib/python3.9/site-packages/mypy/typeshed/stdlib/configparser.pyi: class LegacyInterpolation(Interpolation):
./hexbytes-0.3.0.tar.gz: hexbytes-0.3.0/.tox/py39-lint/lib/python3.9/site-packages/mypy/typeshed/stdlib/configparser.pyi: "LegacyInterpolation",
./hexbytes-0.3.0.tar.gz: hexbytes-0.3.0/.tox/py39-lint/lib/python3.9/site-packages/mypy/typeshed/stdlib/configparser.pyi: class LegacyInterpolation(Interpolation):
./jedi-0.18.2.tar.gz: jedi-0.18.2/jedi/third_party/typeshed/stdlib/3/configparser.pyi: class LegacyInterpolation(Interpolation): ...
./mypy-0.991.tar.gz: mypy-0.991/mypy/typeshed/stdlib/configparser.pyi: "LegacyInterpolation",
./mypy-0.991.tar.gz: mypy-0.991/mypy/typeshed/stdlib/configparser.pyi: class LegacyInterpolation(Interpolation):
./eth-hash-0.5.1.tar.gz: eth-hash-0.5.1/.tox/lint/lib/python3.9/site-packages/mypy/typeshed/stdlib/configparser.pyi: "LegacyInterpolation",
./eth-hash-0.5.1.tar.gz: eth-hash-0.5.1/.tox/lint/lib/python3.9/site-packages/mypy/typeshed/stdlib/configparser.pyi: class LegacyInterpolation(Interpolation):
./eth-account-0.7.0.tar.gz: eth-account-0.7.0/.tox/lint/lib/python3.10/site-packages/mypy/typeshed/stdlib/configparser.pyi: class LegacyInterpolation(Interpolation):
./eth-account-0.7.0.tar.gz: eth-account-0.7.0/.tox/py310-lint/lib/python3.10/site-packages/mypy/typeshed/stdlib/configparser.pyi: class LegacyInterpolation(Interpolation):
./eth-utils-2.1.0.tar.gz: eth-utils-2.1.0/.tox/lint/lib/python3.9/site-packages/mypy/typeshed/stdlib/configparser.pyi: class LegacyInterpolation(Interpolation):
./pytype-2022.11.29.tar.gz: pytype-2022.11.29/pytype/typeshed/stdlib/configparser.pyi: "LegacyInterpolation",
./pytype-2022.11.29.tar.gz: pytype-2022.11.29/pytype/typeshed/stdlib/configparser.pyi: class LegacyInterpolation(Interpolation):
./pylint-2.15.8.tar.gz: pylint-2.15.8/pylint/checkers/stdlib.py: "LegacyInterpolation",
./pyre-check-0.9.17.tar.gz: pyre-check-0.9.17/typeshed/stdlib/configparser.pyi: "LegacyInterpolation",
./pyre-check-0.9.17.tar.gz: pyre-check-0.9.17/typeshed/stdlib/configparser.pyi: class LegacyInterpolation(Interpolation):
./configparser-5.3.0.tar.gz: configparser-5.3.0/src/backports/configparser/__init__.py: "LegacyInterpolation",
./configparser-5.3.0.tar.gz: configparser-5.3.0/src/backports/configparser/__init__.py: class LegacyInterpolation(Interpolation):
./configparser-5.3.0.tar.gz: configparser-5.3.0/src/backports/configparser/__init__.py: "LegacyInterpolation has been deprecated since Python 3.2 "
./configparser-5.3.0.tar.gz: configparser-5.3.0/src/configparser.py: LegacyInterpolation,
./configparser-5.3.0.tar.gz: configparser-5.3.0/src/configparser.py: "LegacyInterpolation",
./configparser-5.3.0.tar.gz: configparser-5.3.0/src/test_configparser.py: elif isinstance(self.interpolation, configparser.LegacyInterpolation):
./configparser-5.3.0.tar.gz: configparser-5.3.0/src/test_configparser.py: elif isinstance(self.interpolation, configparser.LegacyInterpolation):
./configparser-5.3.0.tar.gz: configparser-5.3.0/src/test_configparser.py: elif isinstance(self.interpolation, configparser.LegacyInterpolation):
./configparser-5.3.0.tar.gz: configparser-5.3.0/src/test_configparser.py: class ConfigParserTestCaseLegacyInterpolation(ConfigParserTestCase):
./configparser-5.3.0.tar.gz: configparser-5.3.0/src/test_configparser.py: interpolation = configparser.LegacyInterpolation()
./configparser-5.3.0.tar.gz: configparser-5.3.0/src/test_configparser.py: configparser.LegacyInterpolation()
./eth-rlp-0.3.0.tar.gz: eth-rlp-0.3.0/.tox/lint/lib/python3.9/site-packages/mypy/typeshed/stdlib/3/configparser.pyi: class LegacyInterpolation(Interpolation): ...
./eth-rlp-0.3.0.tar.gz: eth-rlp-0.3.0/venv-erlp/lib/python3.9/site-packages/jedi/third_party/typeshed/stdlib/3/configparser.pyi: class LegacyInterpolation(Interpolation): ...
./eth-rlp-0.3.0.tar.gz: eth-rlp-0.3.0/venv-erlp/lib/python3.9/site-packages/mypy/typeshed/stdlib/3/configparser.pyi: class LegacyInterpolation(Interpolation): ...
./eth_abi-3.0.1.tar.gz: eth_abi-3.0.1/.tox/lint/lib/python3.10/site-packages/mypy/typeshed/stdlib/configparser.pyi: class LegacyInterpolation(Interpolation):

Time: 0:00:17.957695
Found 32 matching lines in 12 projects
```

With colour:

![Same output as above but with the source filename in purple and LegacyInterpolation in orange](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ele6hbe4kix8s0pb6ngu.png)

Answer: very little, mostly backports and type stubs. This told us it's a good candidate
for removal, so a proper `DeprecationWarning` was
[added in Python 3.11](https://docs.python.org/3/whatsnew/3.11.html#standard-library)
(released October 2022) and it will be
[removed in Python 3.13](https://peps.python.org/pep-0387/) (October 2024).

The tool searches using a regex, so you can look for more complicated things like
`"\b(currentThread|activeCount|notifyAll|isSet|isDaemon|setDaemon)\b"`, and it can also
log to file. See `--help` for other options.

Happy searching! 🔎

---

<small>Header photo:
"<a target="_blank" rel="noopener noreferrer" href="https://www.flickr.com/photos/24029425@N06/11237637113">The
card index department</a>" by
<a target="_blank" rel="noopener noreferrer" href="https://www.flickr.com/photos/24029425@N06">Boston
Public Library</a> is licensed under
<a target="_blank" rel="noopener noreferrer" href="https://creativecommons.org/licenses/by/2.0/?ref=openverse">CC
BY 2.0</a>.</small>
