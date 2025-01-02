---
title: "Top PyPI Packages"
date: "2022-05-29T15:53:36.289Z"
tags: ["python", "data", "json", "automation"]
---

[Top PyPI Packages](https://hugovk.github.io/top-pypi-packages/) is a website that
creates a monthly dump of the 5,000 most-downloaded packages from the
[Python Package Index (PyPI)](https://pypi.org/). It provides a human-readable list and
a machine-readable JSON file for programmatic use.

## How it's used

The generated data is important for the Python community: it has been cited by many
academic papers, covering research on topics such as software supply-chain attacks,
genetic algorithms, neural type hints and technical debt.

Websites also use the data for analysing things like community adoption of Python 3 and
of wheels package files, and for automated dependency updates.

Some are [listed here](https://github.com/hugovk/top-pypi-packages/issues/23).

Last but not least, CPython core developers often use the data for community analysis,
for example to check how widespread certain language features are when considering
deprecations and removals, or API changes of Python itself.

Some examples:

https://mail.python.org/archives/search?q=top-pypi-packages

## How it works

It runs on the cheapest DigitalOcean Droplet to query a Google BigQuery dataset from the
Python Software Foundation, and builds the JSON file from that. The data is
automatically committed from the droplet back to the GitHub repository, and GitHub
Actions is used to automatically tag and create a release, which then creates a Digital
Object Identifier (DOI) at Zenodo to help make it citable for researchers.

### In more detail

A "Droplet" is the name DigitalOcean uses for virtual machines, which is basically a
Linux server. I'm using the cheapest $5/month running Ubuntu 20.04 (LTS) plus $1/month
for automated backups. (In July 2022, I'll switch to the new
[$4/month Droplet](https://www.digitalocean.com/try/new-pricing).)

On the first of the month, it runs a cron job:

```crontab
13 11 1 * * ( eval "$(ssh-agent -s)"; ssh-add ~/.ssh/id_rsa-top-pypi-packages; /home/botuser/github/top-pypi-packages/top-pypi-packages.sh ) > /tmp/top-pypi-packages.log 2>&1
```

This
[script](https://github.com/hugovk/top-pypi-packages/blob/c8101970cbfde3aee2eb133ae0d2aa8eb8846a58/top-pypi-packages.sh)
runs
[some](https://github.com/hugovk/top-pypi-packages/blob/c8101970cbfde3aee2eb133ae0d2aa8eb8846a58/build.sh)
[others](https://github.com/hugovk/top-pypi-packages/blob/c8101970cbfde3aee2eb133ae0d2aa8eb8846a58/generate.sh)
to call [pypinfo](https://github.com/ofek/pypinfo/):

```sh
/home/botuser/.local/bin/pypinfo --json --indent 0 --limit 5000 --days  30 "" project > top-pypi-packages-30-days.json
```

[PyPI streams data about downloads to Google BigQuery](https://packaging.python.org/en/latest/guides/analyzing-pypi-package-downloads/)
which are accessible as a public dataset. Google provides a free amount of queries per
month, and I've been adjusting the amount of data fetched to stay within the free quota
(e.g. changing from the top 5k packages to 4k; it used to get data for top packages over
the past 30 days and 365 days, but now only for 30 days; and bumping back up to 5k
packages).

pypinfo is a handy command-line interface (CLI) to access this BigQuery data and dump it
to a JSON file.

Another handy CLI tool called [jq](https://stedolan.github.io/jq/) minifies the JSON
data:

```sh
jq -c . < top-pypi-packages-30-days.json > top-pypi-packages-30-days.min.json
```

These are then committed back to the repo, tagged using [CalVer](https://calver.org/)
(e.g. [2022-05](https://github.com/hugovk/top-pypi-packages/releases/tag/2022.05)) and
pushed.
[GitHub Actions](https://github.com/hugovk/top-pypi-packages/blob/c8101970cbfde3aee2eb133ae0d2aa8eb8846a58/.github/workflows/release.yml)
creates [a release](https://github.com/hugovk/top-pypi-packages/releases) from the tag.

This then creates a
[Digital Object Identifier (DOI) at Zenodo](https://zenodo.org/badge/latestdoi/116806538)
to help make it citable for researchers.

The [website](https://hugovk.github.io/top-pypi-packages/), on GitHub Pages, reads in
the generated JSON file and shows the top 100 (or 1,000 or 5,000) packages in
human-readable form. It's based on [Python Wheels](https://pythonwheels.com), which in
nice circular fashion, uses the JSON data from this project.

## Thanks

Thanks to [PyPI](https://pypi.org/) and
[Google BigQuery](https://cloud.google.com/bigquery/) for the data;
[pypinfo](https://github.com/ofek/pypinfo) and [jq](https://stedolan.github.io/jq/) for
the tools; [Python Wheels](https://pythonwheels.com/) for making their code open source;
and [DigitalOcean](https://m.do.co/c/431978e0c3e9) for sponsoring this project's
hosting. Visit https://do.co/oss-sponsorship to see if your project is eligible.

---

<small>Header photo:
"<a target="_blank" rel="noopener noreferrer" href="https://www.flickr.com/photos/49889874@N05/4772680734">PACKAGES</a>"
by
<a target="_blank" rel="noopener noreferrer" href="https://www.flickr.com/photos/49889874@N05">marc
falardeau</a> is licensed under
<a target="_blank" rel="noopener noreferrer" href="https://creativecommons.org/licenses/by/2.0/?ref=openverse">CC
BY 2.0</a>.</small>
