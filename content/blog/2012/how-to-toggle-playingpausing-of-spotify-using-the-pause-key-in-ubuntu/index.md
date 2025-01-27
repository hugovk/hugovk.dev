---
title: "How to toggle playing/pausing of Spotify using the Pause key in Ubuntu"
date: "2012-01-13T13:05:26Z"
tags: ["linux", "music"]
---

<p>According to <a href="http://www.mabishu.com/blog/2010/11/15/playing-with-d-bus-interface-of-spotify-for-linux/" target="_self" title="Playing with D-Bus interface of Spotify for Linux">Mabishu</a>:</p>
<blockquote>
<p>After a lot of requests from Linux users, Spotify developers have integrated D-Bus support&nbsp;in version 0.4.8.282. So, what this means is simply and awesome! Now Linux developers could use this programmatic interface to interact with Spotify from other apps.</p>
<p>In other words, now is quite simple to send «play», «pause», «move next/previous song» events to Spotify and with this get Spotify fully integrate into our desktop.</p>
</blockquote>
<p>To toggle playing and pausing from the terminal, run:</p>
<p style="padding-left: 30px;"><span style="font-family: 'courier new', courier;">dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause</span></p>
<p>To hook it to the Pause/Break keyboard key:</p>
<ol>
<li>Select System -&gt; Preferences -&gt; Keyboard Shoertcuts</li>
<li>Click Add</li>
<li>Enter any Name: Play or pause Spotify</li>
<li>Paste in the Command:&nbsp;dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause</li>
<li>Click Apply</li>
<li>Click Disabled on the right so it changes to New Shortcut...</li>
<li>Press the Pause/Break key</li>
<li>Click Close</li>
<li>Listen to music in Spotify and press the Pause/Break key to pause or play the music.</li>
</ol>
<p>See the&nbsp;<a href="http://www.mabishu.com/blog/2010/11/15/playing-with-d-bus-interface-of-spotify-for-linux/" target="_self" title="Playing with D-Bus interface of Spotify for Linux">Mabishu</a>&nbsp;post to see how to check the other commands you can hook up to other keys.</p>
<p>(Tested with Ubuntu 10.10 and <a href="http://www.spotify.com/fi/download/previews/" target="_self">Spotify</a>&nbsp;for Linux preview 0.6.291)</p>
