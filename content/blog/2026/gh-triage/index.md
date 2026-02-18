---
title: "A CLI to fight GitHub spam"
date: "2026-02-18T13:35:25Z"
tags: ["gh", "CLI", "triage", "spam", "Python", "CPython"]
featureAlt: "A 19th century illustration of a knight fighting a dragon"
---

## `gh triage spam`

[We](https://github.com/python/cpython/issues?q=sort%3Aupdated-desc%20state%3Aclosed%20label%3Ainvalid)
[get](https://github.com/python/cpython/issues/144900)
[a](https://github.com/python/cpython/issues/144899)
[lot](https://github.com/python/cpython/pull/144806)
[of](https://github.com/python/cpython/issues/144671)
[spam](https://github.com/python/cpython/issues/144654)
[in](https://github.com/python/cpython/issues/144468)
[the](https://github.com/python/cpython/pull/144352)
[CPython](https://github.com/python/cpython/issues/144344)
[project](https://github.com/python/cpython/issues/144296)[.](https://github.com/python/cpython/issues/144275)

A lot of it isn't even [slop](https://en.wiktionary.org/wiki/AI_slop#English), but
mostly worthless "nothing" issues and PRs that barely fill in the issue template, or add
a line of nonsense to some arbitrary file.

They're often from new accounts with usernames like:

- za9066559-wq
- quanghuynh10111-png
- riffocristobal579-cmd
- sajjad5giot
- satyamchoudhary1430-boop
- SilaMey
- standaell1234-maker
- eedamhmd2005-ui
- ksdmyanmar-lighter
- experments-studios
- madurangarathanayaka5-art

A new issue from a username following the pattern `nameNNNN-short_suffix` is a dead
giveaway. I think they're trying to farm "realistic" accounts: open a PR, open an issue,
comment on something, make a fake review.

It's easy but tedious to:

- close the PR/issue as not planned
- retitle to "spam"
- apply the "invalid" label
- remove other labels

I use the GitHub CLI `gh` a lot (for example, `gh co NNN` to check out a PR locally),
and it's straightforward to write your own Python-based extensions, so I wrote
[`gh triage`](https://github.com/hugovk/gh-triage).

Install:

```console
$ gh extension install hugovk/gh-triage
Cloning into '/Users/hugo/.local/share/gh/extensions/gh-triage'...
remote: Enumerating objects: 15, done.
remote: Counting objects: 100% (15/15), done.
remote: Compressing objects: 100% (13/13), done.
remote: Total 15 (delta 5), reused 12 (delta 2), pack-reused 0 (from 0)
Receiving objects: 100% (15/15), 5.09 KiB | 5.09 MiB/s, done.
Resolving deltas: 100% (5/5), done.
✓ Installed extension hugovk/gh-triage
```

Then run like `gh triage spam <issue-or-pr-number-or-url>`:

```console
$ gh triage spam https://github.com/python/cpython/issues/144900
✅ Removed labels: type-bug
✅ Added labels: invalid
✅ Changed title: spam
✅ Closed
```

This can be used for any repo that you have permissions for: it applies the "invalid" or
"spam" labels, but only if they exist in the repo.

Next step: perhaps it could print out the URL to make it easy to report the account to
GitHub (usually for "Spam or inauthentic Activity").

## `gh triage unassign`

Not spam, but another triage helper.

A less common occurrence is a rebase or merge from `main` or change of PR base branch
that ends up bringing in lots of code changes. This often assigns the PR to dozens of
people via
[`CODEOWNERS`](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners),
for example:
[python/cpython#142564](https://github.com/python/cpython/pull/142564#event-21644515910).

Everyone's already been pinged and subscribed to the PR, so it's too late to help that,
but we can automate unassigning them all so at least the PR is not in their "assigned
to" list.

Run `gh triage unassign <issue-or-pr-number-or-url>` to:

- remove all assignees (issues and PRs)
- remove all requested reviewers (PRs only)

For example:

```sh
gh unassign 142564
```

## See also

- [`gh triage` homepage](https://github.com/hugovk/gh-triage)
- Adam Johnson's
  [top `gh` commands](https://adamj.eu/tech/2025/11/24/github-top-gh-cli-commands/)

---

<small>Header photo:
[<i>Otto of the Silver Hand</i> written and illustrated by William Pyle](https://archive.org/details/ottoofsilverhand00pylerich/page/55/mode/1up),
originally published 1888, from the
[University of California Libraries](https://archive.org/details/university_of_california_libraries).</small>
