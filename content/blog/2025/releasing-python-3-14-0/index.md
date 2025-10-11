---
title: "Releasing Python 3.14.0"
date: "2025-10-11T17:04:00Z"
tags: ["python", "python314", "mastodon"]
---

## Prologue

I livetooted the release of Python 3.14.0. Here it is in blogpost form!

---

## One week

Only [one week left](https://peps.python.org/pep-0745/) until the release of
[Python 3.14.0 final](https://docs.python.org/3.14/whatsnew/3.14.html)!

What are you looking forward to?

<small>[#Python](https://mastodon.social/tags/Python)
[#Python314](https://mastodon.social/tags/Python314)<br>
[_Tue, Sep 30, 2025, 15:19 EEST_](https://mastodon.social/@hugovk/115293209822115988)</small>

## Three days

Three days until release and a bug in the Linux kernel has turned a dozen
[buildbots](https://buildbot.python.org/#/release_status) red...

It's already been fixed in the kernel, but will take some time to bubble up. We'll skip
that test for relevant kernel versions in the meantime.

![Python Release Status Dashboard: 3.15-3.13 are red and '✘ Unreleasable: Tier-1 build failed'](buildbots-red.png)

![3.14 Tier-1 build failed (5), Tier-2 build failed (2), Tier-3 build failed (6), Disconnected Tier-1 builder (with recent build) (1), Disconnected Tier-2 builder (1), Disconnected Tier-3 builder (1), Disconnected Tierless builder (1), Warnings from Tier-1 build (1), Warnings from Tier-2 build (3), Warnings from Tier-3 build (2), Unstable build failed (18), Warnings from unstable build (4), Disconnected unstable builder (30), No problem detected (72)](buildbots-details.png)

![ERROR: test_aead_aes_gcm (test.test_socket.LinuxKernelCryptoAPI.test_aead_aes_gcm)](kernel-error.png)

<small>[#Python](https://mastodon.social/tags/Python)
[#Python314](https://mastodon.social/tags/Python314)<br>
[_Sat, Oct 4, 2025, 16:15 EEST_](https://mastodon.social/@hugovk/115316079113681802)</small>

## Green

And back to green!

![Python Release Status Dashboard: 3.15 is red: ✘ Unreleasable Tier-1 build failed. 3.14 is green: ✔ Releasable Disconnected Tier-2 builder. 3.13 is orange: ⚠ Concern Tierless build failed](buildbots-green.png)

<small>[#Python](https://mastodon.social/tags/Python)
[#Python314](https://mastodon.social/tags/Python314)<br>
[_Sun, Oct 5, 2025, 16:58 EEST_](https://mastodon.social/@hugovk/115321909749435460)</small>

## Release day!

First off, check blockers and buildbots.

A new [release-blocker](https://github.com/python/cpython/labels/release-blocker)
appeared yesterday (because of course) but it can wait until 3.14.1.

Three [deferred-blockers](https://github.com/python/cpython/labels/deferred-blocker) are
also waiting until 3.14.1.

A new tier-2 [buildbot](https://buildbot.python.org/#/release_status) failure appeared
yesterday (because of course) but it had previously been offline for a month and will
need some reconfiguration. Can ignore.

OK, let's make a Python!

<small>[#Python](https://mastodon.social/tags/Python)
[#Python314](https://mastodon.social/tags/Python314)
[#release](https://mastodon.social/tags/release)<br>
[_Tue, Oct 7, 2025, 11:40 EEST_](https://mastodon.social/@hugovk/115331985979927140)</small>

## `run_release.py`

Next up, merge and backport the
[final change](https://github.com/python/cpython/pull/139631) to
[What's New in Python 3.14](https://docs.python.org/3/whatsnew/3.14.html) to declare it
latest stable.

Now start `run_release.py`, the main release automation script, which does a bunch of
pre-checks, runs blurb to create a merged changelog, bumps some numbers, and pushes a
branch and tag to my fork. It'll go upstream at the end of a successful build.

Then kick off the [CI](https://github.com/python/release-tools/actions/runs/18308460797)
to build source zips, docs and Android binaries.

![A GitHub Actions build matrix showing an initial verify-input followed by parallel build-source (itself followed by test-source), build-docs, and build-android (consisting of aarch64 and x86_64 jobs).](ci-build.png)

<small>[#Python](https://mastodon.social/tags/Python)
[#Python314](https://mastodon.social/tags/Python314)
[#release](https://mastodon.social/tags/release)<br>
[_Tue, Oct 7, 2025, 12:43 EEST_](https://mastodon.social/@hugovk/115332234337389060)</small>

## Installers

(That's actually the second CI attempt, we had to update some script arguments following
an Android test runner update.)

This build takes about half an hour.

I've also informed the Windows and macOS release managers about the tag and they will
start up installer builds.

This takes a few hours, so I've got time to finish up the release notes.

[PEP 101](https://peps.python.org/pep-0101/) is the full process, but much is automated
and we don't need to follow it all manually.

<small>[#Python](https://mastodon.social/tags/Python)
[#Python314](https://mastodon.social/tags/Python314)
[#release](https://mastodon.social/tags/release)<br>
[_Tue, Oct 7, 2025, 12:52 EEST_](https://mastodon.social/@hugovk/115332266999944269)</small>

## Windows

The
[Windows build](https://dev.azure.com/Python/cpython/_build/results?buildId=164907&view=results)
has been started.

The jobs with profile-guided optimisation (PGO) build once, then collect a profile by
running the tests, and then build again using that profile, to see how 'real' code
executes and optimises for that.

![The Windows build on Azure Pipelines. Lots of boxes for each of 'build binaries', 'sign binaries', 'generate layouts', 'pack', 'test' and finally 'publish'. So far nearing the end of the build binaries stage.](windows-build.png)

Meanwhile, the docs+source+Android build has finished and the artifacts have been copied
to where they need to go with SBOMs created.

<small>[#Python](https://mastodon.social/tags/Python)
[#Python314](https://mastodon.social/tags/Python314)
[#release](https://mastodon.social/tags/release)<br>
[_Tue, Oct 7, 2025, 13:50 EEST_](https://mastodon.social/@hugovk/115332496234142659)</small>

## macOS

The Windows build is ready and macOS is underway.

![Terminal prompt showing the output of run_release.py with lots of checked tasks and ending with: Waiting for files: Linux ✅ Windows ✅ Mac ❌](waiting-for-files.png)

<small>[#Python](https://mastodon.social/tags/Python)
[#Python314](https://mastodon.social/tags/Python314)
[#release](https://mastodon.social/tags/release)<br>
[_Tue, Oct 7, 2025, 15:36 EEST_](https://mastodon.social/@hugovk/115332912443887856)</small>

## Final steps

macOS installer done, next on to the final publishing and announcing steps.

![Terminal showing: ✅ Wait until all files are ready. Go to https://www.python.org/admin/downloads/release/add/ and create a new release. Have you already created a new release for 3.14.0? Enter yes or no:](create-release.png)

<small>[#Python](https://mastodon.social/tags/Python)
[#Python314](https://mastodon.social/tags/Python314)
[#release](https://mastodon.social/tags/release)<br>
[_Tue, Oct 7, 2025, 17:02 EEST_](https://mastodon.social/@hugovk/115333249425273213)</small>

## 🚀 It's out!

🥧 Please install and enjoy
[Python 3.14](https://discuss.python.org/t/python-3-14-0-final-is-here/104210?u=hugovk)!

![Two snakes enjoying a pie with 3.14 on the top and π crimping.](feature.png)

<small>[#Python](https://mastodon.social/tags/Python)
[#Python314](https://mastodon.social/tags/Python314)
[#release](https://mastodon.social/tags/release)<br>
[_Tue, Oct 7, 2025, 17:27 EEST_](https://mastodon.social/@hugovk/115333348041057866)</small>

## Finally

And the last few tasks: announce also on the
[blog](https://blog.python.org/2025/10/python-3140-final-is-here.html) &
[mailing lists](https://mail.python.org/archives/list/python-list@python.org/thread/UDOUFTTWDO7IXHLPQSHTEW2FWGF7ZY2C/),
update the [PEP](https://peps.python.org/pep-0745/) &
[downloads landing page](https://www.python.org/downloads/), fix
[Discourse post](https://discuss.python.org/t/python-3-14-0-final-is-here/104210?u=hugovk)
links, unlock the [`3.14` branch](https://github.com/python/cpython/tree/3.14) for the
core team to start landing PRs that didn't need to be in the RC, and eat the pie.

![A circular lemon meringue pie in front of a Mac showing the release logo.](pie.jpg)

A HUGE thanks to [@sovtechfund](https://mastodon.social/@sovtechfund)
[Fellowship](https://hugovk.dev/blog/2025/im-excited-to-join-the-sovereign-tech-fellowship/)
for allowing me to dedicate my time on getting this out 🎉

<small>[#Python](https://mastodon.social/tags/Python)
[#Python314](https://mastodon.social/tags/Python314)
[#release](https://mastodon.social/tags/release)<br>
[_Tue, Oct 7, 2025, 19:28 EEST_](https://mastodon.social/@hugovk/115333826029083841)</small>
