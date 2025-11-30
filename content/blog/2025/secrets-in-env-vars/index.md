---
title: "Setting secrets in env vars"
date: "2025-11-27T12:55:00Z"
tags: ["security", "1Password", "direnv", "cli"]
featureAlt:
  "An 1895 magazine advert for The Slaymaker Barry Co. showing five padlocks with chunky
  chains and the slogan: 'Bicycle Owners Like Them. Thieves Do Not."
---

Sometimes you need to set environment variables with secrets, API keys or tokens, but
they can be susceptible to exfiltration by malware, as seen during the
[recent Shai-Hulud attack](https://about.gitlab.com/blog/gitlab-discovers-widespread-npm-supply-chain-attack/).

For publishing to PyPI, it's
[strongly recommended to use Trusted Publishing](https://blog.pypi.org/posts/2025-11-26-pypi-and-shai-hulud/)
rather than managing long-lived tokens on your machine.

For other credentials, here's how you can set them as env vars with 1Password CLI and
direnv on macOS.

## 1Password

The 1Password password manager has a
[command-line interface called `op`](<](https://1password.com/downloads/command-line)>).
Thanks to Simon Willison for his useful
[TIL post](https://til.simonwillison.net/macos/1password-terminal) about it.

First [install the CLI](https://developer.1password.com/docs/cli/get-started/):

```sh
brew install 1password-cli
```

Then open 1Password > Settings > Developer > Integrate with 1Password CLI.

Then you can use the `op` command with your password item's name in 1Password:

```console
$ op item get "My secret item" --fields password
[use 'op item get xkm4wrtpvnq8hcjd3yfzs2belg --reveal' to reveal]
```

This obscures the actual password, and gives the item's ID. You can use this ID:

```console
$ op item get xkm4wrtpvnq8hcjd3yfzs2belg --fields password
[use 'op item get xkm4wrtpvnq8hcjd3yfzs2belg --reveal' to reveal]
```

Use `--reveal` to see the actual password:

```console
$ op item get "My secret item" --fields password --reveal
my-secret-password

$ op item get xkm4wrtpvnq8hcjd3yfzs2belg --fields password --reveal
my-secret-password
```

Alternatively, use a
[secret reference](https://developer.1password.com/docs/cli/secret-reference-syntax/).
Open the item in 1Password, next to the password click ⌄ and select Copy Secret
Reference then `op read `it:

```console
$ op read "op://MyVault/xkm4wrtpvnq8hcjd3yfzs2belg/password"
my-secret-password
```

The secret reference is made up of the vault name and item ID, and `op read` doesn't
need `--reveal`.

Take your pick which one you prefer.

## direnv

[direnv](https://direnv.net/) is a handy shell tool that can load and unload environment
variables depending on your current directory.

Next, let's set up direnv so that when you `cd` into a certain directory, it fetches the
password from 1Password and sets it as an env var. When `cd`ing out, the env var is
unloaded.

[Install](https://direnv.net/docs/installation.html) direnv:

```shell
brew install direnv
```

Then [hook direnv into your shell](https://direnv.net/docs/hook.html). If you use
[Oh My Zsh](https://ohmyz.sh/), edit `~/.zshrc` and add `direnv` to the plugins list:

```
plugins=(git gitfast gh you-should-use direnv)
```

Restart/reload your shell:

```
source ~/.zshrc
```

(I first got "Warning: direnv not found. Please install direnv and ensure it's in your
PATH before using this plugin" so needed to move
`eval "$(/opt/homebrew/bin/brew shellenv)"` before `source $ZSH/oh-my-zsh.sh`.)

Now, in your project directory, create a file called `.envrc` containing an env var
export that calls `op`:

```bash
# .envrc
export DEBUG=1
export MY_SECRET=$(op read "op://MyVault/xkm4wrtpvnq8hcjd3yfzs2belg/password")
```

On first run, you need to explicitly allow `direnv` to run for this directory. You also
need to do this when editing `.envrc` later:

```
direnv allow .
```

If 1Password is set up with a passkey, it will now prompt to authorise:

```console
$ cd my-project
direnv: loading ~/my-project/.envrc
direnv: export +DEBUG +MY_SECRET
```

Sometimes it shows a warning because of the 1Password UI prompt, but it's okay:

```console
$ cd my-project
direnv: loading ~/my-project/.envrc
direnv: ([/opt/homebrew/bin/direnv export zsh]) is taking a while to execute. Use CTRL-C to give up.
direnv: export +DEBUG +MY_SECRET
```

Then you can access the env var in your scripts:

```console
$ echo ${DEBUG-nope}
1
$ echo ${MY_SECRET-nope}
my-secret-password
```

But when leaving the directory, you can no longer access it:

```console
$ cd ..
direnv: unloading
$ echo ${DEBUG-nope}
nope
$ echo ${MY_SECRET-nope}
nope
```

## Bonus

1Password offers
[Team accounts to open-source projects](https://github.com/1Password/for-open-source) as
a way of giving back to the open source community.

---

<small>Header photo:
[Slaymaker Barry Co. Sprocket Locks](https://archive.org/details/bearings1218951896cycl/page/n1161/mode/2up)
in
[The Bearings (vol. XII no. 23, 2nd January 1896)](https://library.si.edu/digital-library/book/bearings)
in the [Smithsonian Libraries and Archives](https://library.si.edu/digital-library/),
with [no known copyright restrictions](https://library.si.edu/copyright).</small>
