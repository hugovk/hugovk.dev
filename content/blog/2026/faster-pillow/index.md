---
title: "Speeding up Pillow's open and save"
date: "2026-01-28T10:29:04Z"
tags: ["Python", "python3.15", "pillow", "tachyon", "performance"]
featureAlt: "Pillow and Tachyon logos"
---

## Tachyon

I tried out
[Tachyon](https://docs.python.org/3.15/whatsnew/3.15.html#whatsnew315-sampling-profiler),
the new "high-frequency statistical sampling profiler" coming in
[Python 3.15](https://www.python.org/downloads/latest/python3.15/), to see if we can
speed up the Pillow imaging library. I started with a simple script to open an image:

```python
import sys
from PIL import Image

im = Image.open(f"Tests/images/hopper.{sys.argv[1]}")
```

Then ran:

```console
$ python3.15 -m profiling.sampling run --flamegraph /tmp/1.py png
Captured 35 samples in 0.04 seconds
Sample rate: 1,000.00 samples/sec
Error rate: 25.71
Flamegraph data: 1 root functions, total samples: 26, 169 unique strings
Flamegraph saved to: flamegraph_97927.html
```

Which generates this flame graph:

![Flame graph for opening a PNG with Pillow](flamegraph-png.svg)

The whole thing took 40 milliseconds, with half in `Image.py`'s `open()`. If you visit
the [interactive HTML page](flamegraph_97927.html) we can see `open()` calls
`preinit()`, which in turn imports `GifImagePlugin`, `BmpImagePlugin`, `PngImagePlugin`
and `JpegImagePlugin` (hover over the `<module>` boxes to see them).

Do we really need to import all those plugins when we're only interested in PNG?

Okay, let's try another kind of image:

```console
$ python3.15 -m profiling.sampling run --flamegraph /tmp/1.py webp
Captured 59 samples in 0.06 seconds
Sample rate: 1,000.00 samples/sec
Error rate: 22.03
Flamegraph data: 1 root functions, total samples: 46, 256 unique strings
Flamegraph saved to: flamegraph_98028.html
```

![Flame graph for opening a WebP with Pillow](flamegraph-webp.svg)

Hmm, 60 milliseconds with 80% in `open()` and most of that in `init()`. The
[HTML page](flamegraph_98028.html) shows it imports `AvifImagePlugin`, `PdfImagePlugin`,
`WebpImagePlugin`, `DcxImagePlugin`, `DdsImagePlugin` and `PalmImagePlugin`. We also
have `preinit` importing `GifImagePlugin`, `BmpImagePlugin` and `PngImagePlugin`.

Again, why import _even more_ plugins when we only care about WebP?

## Loading all the plugins?

That's enough profiling, let's look at the code.

When
[`open()`](https://github.com/python-pillow/Pillow/blob/12.1.0/src/PIL/Image.py#L3525)ing
or
[`save()`](https://github.com/python-pillow/Pillow/blob/12.1.0/src/PIL/Image.py#L2536)ing
an image, if Pillow isn't yet initialised, we call a
[`preinit()`](https://github.com/python-pillow/Pillow/blob/12.1.0/src/PIL/Image.py#L327-L369)
function. This loads five drivers for five formats by importing their plugins: BMP, GIF,
JPEG, PPM and PNG.

During import, each plugin
[registers](https://github.com/python-pillow/Pillow/blob/12.1.0/src/PIL/GifImagePlugin.py#L1204-L1211)
its file extensions, MIME types and some methods used for opening and saving.

Then we check each of these plugins in turn to see if one will accept the image. Most of
Pillow's plugins detect an image by opening the file and checking if the first few bytes
match a magic prefix. For example:

- [GIF](https://github.com/python-pillow/Pillow/blob/12.1.0/src/PIL/GifImagePlugin.py#L73-L74)
  starts with `b"GIF87a"` or `b"GIF89a"`.
- [PNG](https://github.com/python-pillow/Pillow/blob/12.1.0/src/PIL/PngImagePlugin.py#L66)
  starts with `b"\211PNG\r\n\032\n"`
  ([reference](https://www.w3.org/TR/PNG-Rationale.html#R.PNG-file-signature)).
- [JPEG](https://github.com/python-pillow/Pillow/blob/12.1.0/src/PIL/JpegImagePlugin.py#L334-L336)
  starts with `b"\xff\xd8\xff"`, where `\xff\xd8` means "Start of Image", and `\xff` is
  the start of the next marker
  ([reference](https://en.wikipedia.org/wiki/JPEG#Syntax_and_structure)).

If none of these five match, we call
[`init()`](https://github.com/python-pillow/Pillow/blob/12.1.0/src/PIL/Image.py#L372-L396),
which imports the remaining 42 plugins. We then check each of these for a match.

This has been the case since at least
[PIL 1.1.1](https://github.com/hugovk/pil-svn.effbot.org/blame/master/PIL/Image.py#L290)
released in 2000 (this is the oldest version I have to check). There were 33 builtin
plugins then and 47 now.

## Lazy loading

This is all a bit wasteful if we only need one or two image formats during a program's
lifetime, especially for things like CLIs. Longer running programs may need a few more,
but unlikely all 47.

A benefit of the plugin system is third parties can
[create their own plugins](https://pillow.readthedocs.io/en/stable/handbook/third-party-plugins.html),
but we can be more efficient with our builtins.

I opened a [PR](https://github.com/python-pillow/Pillow/pull/9398) to add a mapping of
file extensions to plugins. Before calling `preinit()` or `init()`, we can instead do a
cheap lookup, which may save us importing, registering, and checking all those plugins.

Of course, we may have an image without an extension, or with the "wrong" extension, but
that's fine; I expect it's rare and anyway we'll fall back to the original `preinit()`
-> `init()` flow.

After merging the PR, here's a new flame graph for opening PNG
([HTML page](flamegraph_27477.html)):

![Much less compressed flame graph showing less work](flamegraph-png2.svg)

And for WebP ([HTML page](flamegraph_26821.html)):

![Much less compressed for WebP](flamegraph-webp2.svg)

The flame graphs are scaled to the same width, but there's far fewer boxes meaning
there's much less work now. We're down from 40 and 60 milliseconds to 20 and 20
milliseconds.

The PR has a bunch of benchmarks which show opening a PNG (that previously loaded five
plugins) is now 2.6 times faster. Opening a WebP (that previously loaded all 47
plugins), is now 14 times faster. Similarly, Saving PNG is improved by 2.2 times and
WebP by 7.9 times. Success! This will be in Pillow 12.2.0.

## See also

- Henry Schreiner on
  [making packaging faster](https://iscinumpy.dev/post/packaging-faster/).

- Adam Johnson's [tprof](https://adamj.eu/tech/2026/01/14/python-introducing-tprof/) is
  another new tool which is useful for things like this.
