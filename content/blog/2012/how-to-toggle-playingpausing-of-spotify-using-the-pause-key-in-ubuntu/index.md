---
title: "How to toggle playing/pausing of Spotify using the Pause key in Ubuntu"
date: "2012-01-13T13:05:26Z"
tags: ["linux", "music"]
---

According to
[Mabishu](https://web.archive.org/web/20120509091435/http://www.mabishu.com/blog/2010/11/15/playing-with-d-bus-interface-of-spotify-for-linux/):

> After a lot of requests from Linux users, Spotify developers have integrated D-Bus
> support&nbsp;in version 0.4.8.282. So, what this means is simply and awesome! Now
> Linux developers could use this programmatic interface to interact with Spotify from
> other apps.</p>
>
> In other words, now is quite simple to send «play», «pause», «move next/previous song»
> events to Spotify and with this get Spotify fully integrate into our desktop.

To toggle playing and pausing from the terminal, run:

`dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause`

To hook it to the Pause/Break keyboard key:

1. Select System -> Preferences -> Keyboard Shortcuts
2. Click Add
3. Enter any Name: Play or pause Spotify
4. Paste in the Command:
   `dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause`
5. Click Apply
6. Click Disabled on the right so it changes to New Shortcut...
7. Press the Pause/Break key
8. Click Close
9. Listen to music in Spotify and press the Pause/Break key to pause or play the music.

See the
[Mabishu](http://www.mabishu.com/blog/2010/11/15/playing-with-d-bus-interface-of-spotify-for-linux/)
post to see how to check the other commands you can hook up to other keys.

(Tested with Ubuntu 10.10 and
[Spotify](https://web.archive.org/web/20120105155314/https://www.spotify.com/fi/download/previews/)
for Linux preview 0.6.291)
