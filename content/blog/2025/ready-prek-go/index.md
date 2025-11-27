---
title: "Ready prek go!"
date: "2025-09-06T15:50:00Z"
tags: ["python", "prek", "linter", "testing"]
featureAlt:
  "An AH-1G Aircraft Maintenance Test Flight Handbook and handwritten checklist for
  rotary wing helicopters from 1971-1972. Both handbooks are bound with metal rings."
---

I've been using [prek](https://prek.j178.dev/) recently as a drop-in replacement for
[pre-commit](https://pre-commit.com/).

It uses uv for managing Python virtual environments and dependencies, is rewritten in
Rust (because of course) and uses the same `.pre-commit-config.yaml` as pre-commit.

Its homepage says it's not yet production ready, but
[several projects like Apache Airflow and PDM](https://prek.j178.dev/#who-is-using-prek)
are already using it. I've been using it for a while and reporting issues as I find
them; the maintainer is quick with fixes and releases. All the hooks I need are now
supported.

## Getting started

First install using one of the [many methods](https://prek.j178.dev/installation/),
then:

```bash
cd my-repo
pre-commit uninstall       # remove the old hooks
prek install               # install the new hooks
prek run --all-files       # run all lints on all files
git commit -m "my commit"  # run on the changed files in a commit
```

## Benchmarks

prek is noticeably quicker at installing hooks.

> - ⚡ About [10x faster](https://prek.j178.dev/benchmark/) than pre-commit and uses
>   only a third of disk space.

This 10x is a comparison of installing hooks using the excellent
[hyperfine](https://github.com/sharkdp/hyperfine) benchmarking tool.

Here's my own comparison.

- In the first test, I initially ran `pre-commit clean` or `prek clean` to clear their
  caches. I then ran each tool with `run --all-files` in serial on the 126 repos I have
  cloned right now, 84 of which have a `.pre-commit-config.yaml` file. Each then
  downloads and installs the hooks when needed, then runs the lint tools.

- Second, because running the lint tools should be independent and constant time for
  both tools, the next test ran `install-hooks` instead of `run --all files`.

  To get an idea of the amount of work for these two tests, pre-commit reported
  initialising environments 217 times.

- Finally, let's run hyperfine on the
  [Pillow config](https://github.com/python-pillow/Pillow/blob/eef4848a0a7ca0ea5ecd1f647603d85526d88ca7/.pre-commit-config.yaml),
  which installs hooks from 14 repos:

```bash
❯ hyperfine \
--prepare 'rm -rf ~/.cache/prek/ && rm -rf ~/.cache/pre-commit && rm -rf ~/.cache/uv' \
--setup 'prek --version && pre-commit --version' \
'prek install-hooks' \
'pre-commit install-hooks'
```

## Results

|                   | `pre-commit` | `prek` | Times faster |
| ----------------- | ------------ | ------ | ------------ |
| `run --all-files` | 17m13s       | 7m59s  | 2.16         |
| `install-hooks`   | 10m48s       | 2m24s  | 4.50         |
| `hyperfine`       | 39.841s      | 5.539s | 7.19         |

The hyperfine results:

```
Benchmark 1: prek install-hooks
  Time (mean ± σ):      5.539 s ±  0.176 s    [User: 8.973 s, System: 5.692 s]
  Range (min … max):    5.231 s …  5.834 s    10 runs

Benchmark 2: pre-commit install-hooks
  Time (mean ± σ):     39.841 s ±  2.017 s    [User: 19.760 s, System: 8.203 s]
  Range (min … max):   36.930 s … 43.976 s    10 runs

Summary
  prek install-hooks ran
    7.19 ± 0.43 times faster than pre-commit install-hooks
```

Give it a try and give it a [⭐](https://www.star-history.com/#j178/prek&Date)!

## Bonus

These are the aliases I have set for pre-commit and prek:

```bash
alias pci="pre-commit install --allow-missing-config"
alias pcu="pre-commit uninstall"
alias pca="pre-commit autoupdate --jobs 0"
alias pcr="pre-commit run --all-files"
alias pki="prek install --allow-missing-config"
alias pku="prek uninstall"
alias pka="prek autoupdate --jobs 0"
alias pkr="prek run --all-files"
```

Where:

- `install`'s `--allow-missing-config` prevents failing with an error code when a repo
  has no config file
- `autoupdate`'s `--jobs 0` uses all the available threads to make it faster

---

<small>Header photo:
<a target="_blank" rel="noopener noreferrer" href="https://www.flickr.com/photos/sdasmarchives/51500757435/">AH-1G
Aircraft Maintenance Test Flight Handbook and handwritten checklist for helicopters</a>
in the
<a target="_blank" rel="noopener noreferrer" href="https://www.flickr.com/photos/sdasmarchives/">San
Diego Air and Space Museum Archive</a>, with
<a target="_blank" rel="noopener noreferrer" href="https://www.flickr.com/commons/usage/">no
known copyright restrictions</a>.</small>
