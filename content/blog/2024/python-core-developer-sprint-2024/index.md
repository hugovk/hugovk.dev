---
title: "Python Core Developer Sprint 2024"
date: "2024-10-05T19:39:48.918Z"
tags: ["python", "sprint", "coredevsprint", "2024"]
---

🐍🏃The week before last was the annual Python Core Dev Sprint, graciously hosted by
Meta in Bellevue, WA!

The idea: bring a bunch of Python core team members, triagers, and special guests to the
same room for a week. It's hugely beneficial and productive, we held many in-depth
discussions that just don't happen when we're all remote and async, and got to work on
many different things together.

![A panoramic shot of a room of people, some sitting at desks, some standing, some working on laptops, some in discussion.](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/5rpkesswa2xbczkuwoq7.jpeg)

<center><small>The sprint room</small></center>

During the week, I reviewed 39 PRs, created 15, merged 10, updated 4, and closed 2
issues.

## Monday highlights

As release manager for [Python 3.14](https://peps.python.org/pep-0745/), I discussed
with [Brett Cannon](https://fosstodon.org/@brettcannon) one of his project ideas which
will come after lock files, and after the next big one.

Also as RM, discussed with [Russell Keith-Magee](https://cloudisland.nz/@freakboy3742),
Ned Deily, [Łukasz Langa](https://mastodon.social/@ambv) and
[Thomas Wouters](https://social.coop/@Yhg1s) about
[including official binaries for iOS and Android](https://beeware.org/news/buzz/2024q4-roadmap/),
which wandered into ideas about security releases.

I did some maintenance of our PyPI projects, adding
[PEP 740 attestations](https://peps.python.org/pep-0740/), support for the
[new Python 3.13](https://peps.python.org/pep-0719/) and dropping support for the
[very-nearly-EOL 3.8](https://peps.python.org/pep-0569/).

## Tuesday highlights

Started investigating slow doctest on 3.13+ with
[Alex Waygood](https://fosstodon.org/@AlexWaygood), who on Wednesday narrowed it down to
a problem with the
[new incremental garbage collector](https://github.com/python/cpython/issues/124567),
which would go on to be reverted by Friday and result in
[Python 3.13's Monday release to be postponed and replaced with an extra release candidate](https://discuss.python.org/t/python-3-12-7-and-3-13-0rc3-released/66306?u=hugovk).
Not ideal, but much better to discover these things before the big release.

We had a Q&A session with the Steering Council:
[Barry Warsaw](https://mastodon.social/@pumpichank), Emily Morehouse,
[Gregory P. Smith](https://infosec.exchange/@gpshead), Pablo Galindo Salgado and Thomas.

![The steering council: Barry, Emily, Greg with a microphone, Pablo and Thomas sitting on high stools.](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/g7yyzyqtztoednyacr1r.jpg)

<center><small>The Python Steering Council</small></center>

Proofread Guido van Rossum's
[STAR voting proposal](https://discuss.python.org/t/changing-pep-13-to-adopt-bloc-star-voting/64971?u=hugovk)
for electing future steering councils.

Discussed with Eric Snow his novel method for displaying many code samples in a table,
using `<details>` disclosures to prevent the table being too wide. Looks like a good
solution!

## Wednesday highlights

I applied the [finishing touches](https://github.com/python/peps/pull/3995) to
[PEP 2026](https://peps.python.org/pep-2026/) (Calendar versioning for Python) and Barry
gave it a final review. Ready for submission!

[Seth Larson](https://fosstodon.org/@sethmlarson), the PSF
[Security Developer-in-Residence](https://sethmlarson.dev/security-developer-in-residence),
wasn't at the sprint but we discussed our plan to stop providing GPG signatures for
CPython and rely on SigStore instead. Expect a PEP soon!

Also not at the sprint, I recommended PSF
[Infrastructure Engineer](https://pyfound.blogspot.com/2024/07/announcing-our-new-infrastructure.html)
[Jacob Coffee](https://fosstodon.org/@Monorepo) as a [CPython triager](CPython). Welcome
aboard!

The whole room discussed including
[static type annotations in CPython](https://discuss.python.org/t/static-type-annotations-in-cpython/65068?u=hugovk).

We had a Q&A session with two of the three Developers-in-Residence, Łukasz and
[Petr Viktorin](https://mastodon.social/@encukou).

![Łukasz (with a microphone) and Petr sitting on high stools.](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/vbn0yvsz7t9t2j7yfd2j.jpg)

<center><small>Q&A with Łukasz and Petr</small></center>

Discussed
[expanding the voter pool for Steering Council elections](https://discuss.python.org/t/collecting-feedback-about-expanding-the-voter-pool-for-sc-elections?u=hugovk)
with [Mariatta](https://fosstodon.org/@mariatta), Greg and Thomas.

Larry Hastings handed out, in return for _oohs_ and _aahs_, some nice P.C.D.S. 2024
stickers he generously designed and printed up for us. Thanks!

![Two stickers. One yellow snake with its body looping and spelling out the letters PCDS (for Python Core Dev Sprint), one blue snake spelling 2024.](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/arqsq2qg7h1giiko2g40.jpg)

<center><small>PCDS 2024 stickers by Larry</small></center>

## Thursday highlights

On the 26th September, at 10:26 Bellevue time (20:26 Helsinki time), I
[submitted PEP 2026 to the Steering Council!](https://github.com/python/steering-council/issues/255)🤞

Brett discussed whether we should update
[PEP 387 to prefer 5 year deprecations instead of 2 years](https://discuss.python.org/t/updating-pep-387-to-prefer-5-year-deprecations-instead-of-2-years/65166?u=hugovk).

Brandt Bucher gave us all an update on the progress of the Just-in-Time (JIT) compiler
("we went from 0% slower to 0% faster!") and we discussed plans for Python 3.14.

Because I couldn't attend Thursday's
[Helsinki Python meetup](https://helsinki-python.github.io/) due to being at another
kind of Python meetup on the other side of the world, I gave the famous HelPy quiz to
the assembled core devs. Unsurprisingly they did pretty well, but the most incorrect
answer was a pleasant surprise: we've had ~400 not ~80 new contributors to Python 3.13!

Pablo performed card tricks!

![Pablo splaying open a deck of PyCon US playing cards and Greg picking one.](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/tlusli7ylxa3di48nmct.jpg)

<center><small>Magic from Pablo</small></center>

Meta took us out for a delicious dinner at a local fish restaurant. Thank you!

## Friday highlights

Mariatta presented ideas to Jelle Zijlstra, Petr, Russell and me about to use modern
tools to create a modern, interactive tutorial.

Also during the week, continued work with Adam Turner on improving the
[docs.python.org](https://docs.python.org/3/) build. Adam wasn't at the sprint, so
tag-teamed PR reviews overnight. After
[much work straddling many teams, projects and repos](https://github.com/python/docsbuild-scripts/issues/169#issuecomment-2389743956),
we've got the full HTML build loop for 13 languages × 3 versions down from over 40 hours
to just under 9 hours, with more improvements coming.

Made a [demo](https://hugovk-cpython.readthedocs.io/en/pydata-sphinx-theme/) of the
CPython docs using the
[PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/).

Along with around 25 others, I was on Łukasz and Pablo's
[core.py podcast](https://podcasters.spotify.com/pod/show/corepy/episodes/Episode-15-Core-sprint-at-Meta-e2p64tc).

![Łukasz and Pablo in their ad-hoc podcast studio in a Meta meeting room.](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/obqejp8n5acztsb8knaq.jpg)

<center><small>Łukasz and Pablo in their ad-hoc podcast studio in a Meta meeting room</small></center>

Itamar gave us cake for the podcast's first birthday!

![A big white cake, with decorations of Łukasz and Pablo's faces, along with the Core.py logo, a big digit 1, headphones, microphone, bananas, and "emosido engañado" graffiti.](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/8gz97wzjn5khsjg4anln.jpg)

<center><small>cake.py. Photo by Itamar Oren.</small></center>

## Thank you

It was a hugely productive week, big thanks to Itamar Oren and Meta for organising and
hosting!

See also Mariatta's excellent [blog posts](https://mariatta.ca/tags/sprint/), and I
recommend the
[core.py podcast](https://podcasters.spotify.com/pod/show/corepy/episodes/Episode-15-Core-sprint-at-Meta-e2p64tc)
with short interviews with some 25 attendees! Łukasz and Pablo were also guests on the
[Changelog podcast](https://changelog.com/podcast/611) during the sprint.

---

<small>Header photo by Itamar Oren</small>
