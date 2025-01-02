---
title: "Bits of Pluto on Mastodon"
date: "2023-02-18T13:16:49.297Z"
tags: ["linodehackathon", "mastodon", "opensource", "bots"]
---

## What I built

I built a Mastodon bot that posts a a different bit of Pluto every six hours.

### Category Submission

Wacky Wildcard

### App Link

https://botsin.space/@bitsofpluto

### Screenshots

<center>https://botsin.space/@bitsofpluto/109854013035140138</center>

![Dark shadows caused by mountains](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/r78gpvcyl5ai09z93cds.png)

---

<center>https://botsin.space/@bitsofpluto/109878078918934666</center>

![Red cratered area to the left giving way to creamy pale plain to the right](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/7zlvfcqdh1nj4nlgpl9p.png)

---

<center>https://botsin.space/@bitsofpluto/109882325572738354</center>

![Long ridges causing shadows](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/fr8oxtml9trqb7kg1ptj.png)

---

<center>https://botsin.space/@bitsofpluto/109872416513104327</center>

![Reddish area with many craters, including a large crater with a central peak](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ys3xv8itck0jpjfttqjq.png)

---

<center>https://botsin.space/@bitsofpluto/109869584884331747</center>

![Mostly space with a sliver of surface in the corner](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/tevx5s0kxjsq1kwlm847.png)

---

<center>https://botsin.space/@bitsofpluto/109835610772369900</center>

![Deep red with ridges, and the curve of Pluto against deep black space](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/wscpk9b699sexhly1es7.png)

---

<center>https://botsin.space/@bitsofpluto/109828532816033685</center>

![Mostly pale surface with mountainous areas and craters](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/144ix05imzd5dv3qvmpr.png)

---

<center>https://botsin.space/@bitsofpluto/109845519798723221</center>

![Mixed white and red surface pocked with many craters](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/68l14un3lt032llpcnl7.png)

### Description

Bits of Pluto posts a different bit of Pluto to Mastodon every six hours. Each is a crop
from an image by NASA's New Horizons spacecraft.

### Link to Source Code

https://github.com/hugovk/bitsofpluto

### Permissive License

MIT

## Background

For decades, Pluto had only been a speck of light until the NASA's Hubble Space
Telescope captured it in
[never-before-seen detail](https://hubblesite.org/contents/news-releases/2010/news-2010-06.html):

![NASA: "Hubble's view isn't sharp enough to see craters or mountains, if they exist on the surface, but Hubble reveals a complex-looking and variegated world with white, dark-orange, and charcoal-black terrain."](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/tvnfv986pgdognhevi3j.jpg)

Just a few years later, I followed the journey of NASA's New Horizons spacecraft in awe
as it flew past Pluto, in the far depths of our solar system.

Like many others I was especially struck by the beautiful photographs it shot,
especially this large, detailed image:

![Pluto in enhanced colour](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/x3cu2253wz13viuoyg3y.png)

As NASA describe it:

> NASA’s New Horizons spacecraft captured this high-resolution enhanced color view of
> Pluto on July 14, 2015. The image combines blue, red and infrared images taken by the
> Ralph/Multispectral Visual Imaging Camera (MVIC). Pluto’s surface sports a remarkable
> range of subtle colors, enhanced in this view to a rainbow of pale blues, yellows,
> oranges, and deep reds. Many landforms have their own distinct colors, telling a
> complex geological and climatological story that scientists have only just begun to
> decode. The image resolves details and colors on scales as small as 0.8 miles (1.3
> kilometers). The viewer is encouraged to zoom in on the
> [full resolution](http://www.nasa.gov/sites/default/files/thumbnails/image/crop_p_color2_enhanced_release.png)
> image on a larger screen to fully appreciate the complexity of Pluto’s surface
> features.

I second the recommendation to zoom in on the full resolution! The detail and is
astounding, especially compared to the Hubble image.

I thought it would be fascinating to chop this up and put it in a social media feed to
enjoy different aspects of the detail, to punctuate the doomscrolling with a moment of
wonder.

### How I built it

I built the bot in Python. Originally it posted to Twitter, but as the future of bots on
Twitter is
[less](https://www.theverge.com/2023/2/2/23582982/twitter-api-free-access-cutoff-bot-developers-shutdown)
[than](https://www.theverge.com/2023/2/2/23582982/twitter-api-free-access-cutoff-bot-developers-shutdown)
[certain](https://www.vice.com/en/article/4axzzd/twitters-latest-chaotic-move-will-kill-the-sites-best-bots-account-owners-say),
the time was ready to port it over to
[Mastodon](https://botwiki.org/resources/fediverse-bots/) where bots are welcome.

On the way, I learned how to calculate brightness in images, how to use the Mastodon
API, and how to set up a bot on Linode and (the appropriately-named!) botsin.space.

The bot does two things:

1. Get a bit of Pluto
2. Post to Mastodon

#### 1. Get a bit of Pluto

The
[`bitsofpluto()` function](https://github.com/hugovk/bitsofpluto/blob/d98c8fe4749c31c4d142b89a06d0241773794f00/bitsofpluto.py#L92-L139)
takes a single parameter, the path to the full resolution Pluto image.

The image is opened using [Pillow](https://pillow.readthedocs.io/).

We then choose a random width for the image, somewhere between 800 and 2000 pixels, with
height is set to ¾ the width. This is to give a different zoom level each time. We then
randomly select a window to crop. This is our potential bit of Pluto.

But we don't stop there. The image has quite a large background of empty black (or
nearly black) space. We don't want to post that. So we sample 9 points from the image
(corners, centre point, and bisecting points) and measure the brightness where 0 is
black and 255 is white. If brightness is under 10, we count it as a dark point. If there
are 6 or less, we save the image to a temporary directory.

Otherwise if there are too many dark points, we discard this crop, and start again from
the top. I came up with these figures of 10 and 7 through trial-and-error. It's quite
nice to sometimes get an image with a
[corner of Pluto's curvature against the darkness of space](https://botsin.space/@bitsofpluto/109880910091459752):

![Light surface of Pluto with a few cratered, the darkness of space behind](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/sh69yjordzcx0q0p20o1.png)

#### 2. Post to Mastodon

We use the [Mastodon.py library](https://mastodonpy.readthedocs.io/) to via the Mastodon
API.

The
[`toot_it() function`](https://github.com/hugovk/bitsofpluto/blob/d98c8fe4749c31c4d142b89a06d0241773794f00/bitsofpluto.py#L46-L89)
first reads in the credentials for posting. I generated them using a
[helper script](https://github.com/hugovk/mastodon-tools/blob/main/mastodon_create_app.py)
I wrote based upon [Allison Parrish](https://www.decontextualize.com/)'s
[instructions](https://gist.github.com/aparrish/661fca5ce7b4882a8c6823db12d42d26).

Once authenticated, there's a two-step process for posting:

1. Upload the image using `api.media_post()`, which returns a reference to the media
2. Create the Mastodon post, using the media reference

#### Hosting

##### Linode

The bot code is hosted on Linode. The nice thing about Mastodon bots is that they rarely
need expensive or high-end hosting. I created a Linode using the cheapest option: for
$5/month the "Nanode 1 GB" plan gives 1 GB RAM, 1 CPU and 25 GB storage, more than
enough for our needs.

![Linode 24-hour usage stats: average 0.43% CPU usage, and about ~1 Kb/s average network both inbound and outbound](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/6oiwss0gys3ndhlnsksj.png)

I chose a Ubuntu 22.04 LTS image: LTS means "long-term support", it will be supported
for 5 years, until April 2027. And I chose the Frankfurt, DE region because it's closest
to me.

After creating a user, I logged in via SSH, and cloned the
[bitsofpluto repo](https://github.com/hugovk/bitsofpluto).

I ran `crontab -e` to schedule it to run once every six hours:

```cron
0 */6 * * * /home/botuser/bin/scheduled/0000-06-repeat.sh > /tmp/logs/0000-06-repeat.log
```

Where `0000-06-repeat.sh` contains:

```sh
#!/bin/bash
#set -e

mkdir -p /tmp/logs/

~/github/bitsofpluto/crontask.sh  > /tmp/logs/bitsofpluto.log 2>&1
```

Which, when the cron triggers, switches to the repo, fetches any recent changes, and
then runs the bot to make a post:

```sh
python3 bitsofpluto.py --yaml ~/bin/data/bitsofpluto.yaml --no-web
```

##### botsin.space

The bot's Mastodon account is on [Colin Mitchell](https://muffinlabs.com/)'s
[botsin.space instance](https://botsin.space/about), home to many other
[excellent bots](https://botsin.space/public/local).

### Additional Resources/Info

I've made two other Mastodon bots:

- [@tiny_bus_stop](https://botsin.space/@tiny_bus_stop) -
  [uses Tracery](https://github.com/hugovk/cheapbotsdonequick/blob/main/tiny_bus_stop.json)
  and [Cheap Bots, Toot Sweet!](https://cheapbotstootsweet.com/)
- [@FlagFacts](https://botsin.space/@FlagFacts) -
  [uses Python](https://github.com/hugovk/randimgbot)

Enjoy!
