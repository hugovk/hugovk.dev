---
title: "My most used command-line commands"
date: "2025-04-04T16:50:00Z"
tags: ["CLI", "terminal"]
featureAlt: "Close-up a typewriter's typebars"
---

Following
[Jeff Triplett's lead](https://micro.webology.dev/2025/01/02/my-most-used-commands-in/),
here's a list of my most used terminal commands.

| No. | Total | Command        | Info                                                                                                                                                           |
| --- | ----- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.  | 1239  | `rg`           | [ripgrep](https://github.com/BurntSushi/ripgrep)                                                                                                               |
| 2.  | 1038  | `c`            | aliased to [`pycharm`](https://www.jetbrains.com/pycharm/)                                                                                                     |
| 3.  | 847   | `gc`           | aliased to `git commit --verbose` via [Oh My Zsh](https://github.com/ohmyzsh/ohmyzsh) [Git plugin](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/git) |
| 4.  | 559   | `gco`          | aliased to `git checkout`                                                                                                                                      |
| 5.  | 518   | `git`          |                                                                                                                                                                |
| 6.  | 384   | `./python.exe` | Python [built from source](https://devguide.python.org/) on macOS                                                                                              |
| 7.  | 365   | `cd`           |                                                                                                                                                                |
| 8.  | 359   | `cat`          | aliased to [`bat -p`](https://github.com/sharkdp/bat)                                                                                                          |
| 9.  | 336   | `gs`           | aliased to `scmpuff_status` via [scmpuff](https://mroth.github.io/scmpuff/) to give numeric shortcuts for files                                                |
| 10. | 326   | `gl`           | aliased to `git log` via Oh My Zsh Git plugin                                                                                                                  |
| 11. | 315   | `gb`           | aliased to `git branch` via Oh My Zsh Git plugin                                                                                                               |
| 12. | 308   | `p`            | aliased to `python`                                                                                                                                            |
| 13. | 263   | `ga`           | aliased to `git add` via Oh My Zsh Git plugin                                                                                                                  |
| 14. | 227   | `l`            | aliased to `ls -lah`                                                                                                                                           |
| 15. | 214   | `uv`           | [Python package manager](https://docs.astral.sh/uv/)                                                                                                           |
| 16. | 203   | `f`            | aliased to `find . \| rg` (TODO: learn [`fd`](https://github.com/sharkdp/fd))                                                                                  |
| 17. | 189   | `python`       |                                                                                                                                                                |
| 18. | 175   | `gd`           | aliased to `git diff` via Oh My Zsh Git plugin                                                                                                                 |
| 19. | 174   | `rm`           |                                                                                                                                                                |
| 20. | 165   | `em`           | the [CLI emoji keyboard](https://github.com/hugovk/em-keyboard)                                                                                                |
| 21. | 164   | `gh`           | aliased to `GH_PAGER="less -FRX" gh`, mostly for `gh co <PR number>`, sometimes `gh cache delete --all`                                                        |
| 22. | 145   | `open`         |                                                                                                                                                                |
| 23. | 120   | `mv`           |                                                                                                                                                                |
| 24. | 120   | `make`         | for building Python, docs, devguide and PEPs                                                                                                                   |
| 25. | 117   | `cp`           |                                                                                                                                                                |
| 26. | 116   | `tox`          |                                                                                                                                                                |
| 27. | 116   | `pypi`         | see below                                                                                                                                                      |
| 28. | 111   | `bc`           | aliased to `/usr/local/bin/bcompare` [Beyond Compare](https://www.scootersoftware.com/) diff tool                                                              |
| 29. | 110   | `piu`          | aliased to `uv pip install --system -U`                                                                                                                        |
| 30. | 110   | `pcr`          | aliased to `pre-commit run --all-files`                                                                                                                        |

`pypi` is a little function in my dotfiles for opening the PyPI page for a package,
either `pypi <package>` or let it try and guess the name from the current directory:

```sh
pypi () {
	if [ "$1" = "" ]
	then
		local name=$(python setup.py --name)
	else
		local name=$1
	fi
	echo $name
	open https://pypi.org/project/"$name"/
}
```

The macOS/iTerm/Oh My Zsh command to get this list:

`history | awk '{print $2}' | sort | uniq --count | sort --numeric-sort --reverse | head -30`

---

<small>Header photo: Close-up the typebars of a Olympia Büromaschinenwerke A.G. Erfurt
typewriter
(<a target="_blank" rel="noopener noreferrer" href="https://creativecommons.org/licenses/by-nc-sa/2.0/">CC
BY-NC-SA 2.0</a>
[Hugo van Kemenade](https://www.flickr.com/photos/hugovk/1482906651/)).</small>
