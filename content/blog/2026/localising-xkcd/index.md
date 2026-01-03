---
title: "Localising xkcd"
date: "2026-01-03T14:06:51Z"
tags: ["Python", "python3.14", "xkcd", "PyCon"]
featureAlt: "xkcd comic: [Mrs. Roberts receives a call from her son's school on her wireless phone. She is standing with a cup of hot coffee or tea (shown with a small line above the cup) facing a small round three-legged table to the right. The voice of the caller is indicated to come from the phone with a zigzag line.]
Voice over the phone: Hi, This is your son's school. We're having some computer trouble.
[In this frame-less panel Mrs. Roberts has put the cup down on the table turned facing out.]
Mrs. Roberts: Oh, dear – did he break something?
Voice over the phone: In a way –
[Mrs. Roberts is now drinking from the cup again looking right. The table is not shown.]
Voice over the phone: Did you really name your son Robert'); DROP TABLE Students;-- ?
Mrs. Roberts: Oh, yes. Little Bobby Tables, we call him.
[Mrs. Roberts holds the cup down.]
Voice over the phone: Well, we've lost this year's student records. I hope you're happy.
Mrs. Roberts: And I hope you've learned to sanitize your database inputs."
---

I gave a lightning talk at a bunch of conferences in 2025 about some of the exciting new
things coming in [Python 3.14](https://hugovk.dev/blog/2025/and-now/), including
[template strings](https://t-strings.help/).

One thing we can use t-strings for is to prevent SQL injection. The user gives you an
untrusted t-string, and you can sanitise it, before using it in a safer way.

I illustrated this with [xkcd 327](https://xkcd.com/327/), titled "Exploits of a Mom",
but commonly known as "Little Bobby Tables".

I localised most of the slides for the PyCon I was at, including this comic. Here they
are!

## PyCon Italia

_May, Bologna_

![Did you really name your son Roberto'); DROP TABLE Students;-- ? Oh, yes. Piccolo Berto Tables, we call him.](italia.png)

## PyCon Greece

_August, Athens_

![Did you really name your son Κωνσταντίνος'); DROP TABLE Students;-- ? Oh, yes. Μικρός Ντίνος Tables, we call him.](greece.png)

## PyCon Estonia

_October, Tallinn_

![Did you really name your son Raivo'); DROP TABLE Students;-- ? Oh, yes. Pisikene Tables, we call him.](estonia.png)

## PyCon Finland

_October, Jyväskylä_

![Did you really name your son Juhani'); DROP TABLE Students;-- ? Oh, yes. Pikku Jussi, we call him.](finland.png)

## PyCon Sweden

_October, Stockholm_

![Did you really name your son Oskar'); DROP TABLE Students;-- ? Oh, yes. Lille Ogge Bord, we call him.](sweden.png)

## Thanks

Thanks to Randall Munroe for licensing the comic under the
[Creative Commons Attribution-NonCommercial 2.5 License](https://creativecommons.org/licenses/by-nc/2.5/).
These adaptations are therefore licensed the same way.

Finally, here's links for 2026, I recommend them all:

- [PyCon Italia, 27-30 May](https://2026.pycon.it/en): the
  [CFP](https://2026.pycon.it/en/call-for-proposals) is open until 6th January
- [PyCon Estonia, 8-9 October](https://pycon.ee/)
- [PyCon Greece, 12-13 October](https://2026.pycon.gr/)
- [PyCon Sweden, TBA](https://pycon.se/)
- [PyCon Finland, TBA](http://fi.pycon.org/)
