---
title: "Morse Texter"
date: "2005-05-30T17:07:09Z"
tags: ["S60"]
---

After reading [this](https://www.russellbeattie.com/blog/1008476.html) and
[this](https://web.archive.org/web/20050526230439/http://muddybranch.thejkgroup.com/2005/05/morse_code_trum.html)
and [this](https://www.m0tzo.co.uk/2004/01/11/morse-code-software/) I decided to knock
up this ~~dodgy prototype~~
[amazing application](https://web.archive.org/web/20110122015431/http://morsetexter.googlecode.com/files/MorseTexter.sis)
for S60 v2.x phones (but not v1.x or v3.x -- check your version
[here](<https://en.wikipedia.org/wiki/S60_(software_platform)>). Tap in some Morse code,
and then send it as an SMS. Keys are:

- 1, 4, 7, or \* - Dot
- 2, 5, 8, or 0 - Space
- 3, 6, 9, or # - Dash
- Left arrow - Dot
- OK key - Space
- Right arrow - Dash
- C key - Delete last dot, dash or letter
- Call/green key - Send as SMS

For a gap between letters, press space once. For a gap between words, press space a
second time.

Here's the
[source](https://web.archive.org/web/20160328104543/https://morsetexter.googlecode.com/files/MorseTexter.zip)
([Google Code](https://code.google.com/archive/p/morsetexter/),
[GitHub](https://github.com/hugovk/morsetexter)), do whatever you want with it. Some
ideas:

- Add short and long key press handling on the OK key for dot and dash input, with
  proper timing to add character and word spaces
- Centre the Morse characters and make them bigger/bolder
- [More ideas](https://www.m0tzo.co.uk/2004/01/11/morse-code-software/)

. / -. / .--- / --- / -.-- / -.-.--
