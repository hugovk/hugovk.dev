---
title: "TIL: exclude_also with coverage.py"
date: "2023-11-06T20:05:55.767Z"
tags: ["python", "today-i-learned", "coverage", "coveragepy"]
---

Sometimes you have code you want to exclude from the test coverage report, because it
doesn't really make sense to test it.

For example, maybe you want to exclude:

```python
if __name__ == "__main__":
    main()
```

The _old_ advice was to add something like this to `.coveragerc`:

```ini
[report]
# Regexes for lines to exclude from consideration
exclude_lines =
    # Have to re-enable the standard pragma:
    pragma: no cover

    # Don't complain if non-runnable code isn't run:
    if __name__ == .__main__.:
```

But since
[coverage.py 7.2.0 (2023-02-22)](https://coverage.readthedocs.io/en/7.3.2/changes.html#version-7-2-0-2023-02-22)
you can use `exclude_also` instead and skip that pragma:

```ini
[report]
# Regexes for lines to exclude from consideration
exclude_also =
    # Don't complain if non-runnable code isn't run:
    if __name__ == .__main__.:
```

Which is:

```diff
 [report]
 # Regexes for lines to exclude from consideration
-exclude_lines =
-    # Have to re-enable the standard pragma:
-    pragma: no cover
-
+exclude_also =
     # Don't complain if non-runnable code isn't run:
     if __name__ == .__main__.:
```

## Thanks

To [Brian Okken](https://mastodon.social/@brianokken@fosstodon.org/111360201593749157)
for the tip.

To [Ned Batchelder](https://nedbatchelder.com/) for maintaining
[Coverage.py](https://coverage.readthedocs.io).

To the Library of Congress and Flickr Commons for the photo of a
[covered wagon](https://www.flickr.com/photos/library_of_congress/52303625278/).
