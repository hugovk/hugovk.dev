---
title: "Replacing python-dateutil to remove six"
date: "2025-12-29T16:53:00Z"
tags: ["python", "dateutil", "six"]
featureAlt:
  "Two panel woodcut. On the left, an almost stick figure carrying a Christmas tree
  through dark woodland. On the right, a Jugendstil calendar with highly stylised
  letters for December, the days in German and numbers."
---

The dateutil library is a popular and powerful Python library for dealing with dates and
times.

However, it still supports Python 2.7 by
[depending on the six compatibility shim](https://sethmlarson.dev/winning-a-bet-about-six-the-python-2-compatibility-shim),
and I'd prefer not to install for Python 3.10 and higher.

Here's how I replaced three uses of its
[`relativedelta`](https://dateutil.readthedocs.io/en/stable/relativedelta.html) in a
couple of CLIs that didn't really need to use it.

## One

[norwegianblue](https://github.com/hugovk/norwegianblue/pull/267) was using it to
calculate six months from now:

```python
import datetime as dt

from dateutil.relativedelta import relativedelta

now = dt.datetime.now(dt.timezone.utc)
# datetime.datetime(2025, 12, 29, 15, 59, 44, 518240, tzinfo=datetime.timezone.utc)
six_months_from_now = now + relativedelta(months=+6)
# datetime.datetime(2026, 6, 29, 15, 59, 44, 518240, tzinfo=datetime.timezone.utc)
```

But we don't need to be so precise here, and 180 days is good enough, using the standard
library's
[`datetime.timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta):

```python
import datetime as dt

now = dt.datetime.now(dt.timezone.utc)
# datetime.datetime(2025, 12, 29, 15, 59, 44, 518240, tzinfo=datetime.timezone.utc)
six_months_from_now = now + dt.timedelta(days=180)
# datetime.datetime(2026, 6, 27, 15, 59, 44, 518240, tzinfo=datetime.timezone.utc)
```

## Two

[pypistats](https://github.com/hugovk/pypistats/pull/519) was using it get the last day
of a month:

```python
import datetime as dt

first = dt.date(year, month, 1)
# datetime.date(2025, 12, 1)
last = first + relativedelta(months=1) - relativedelta(days=1)
# datetime.date(2025, 12, 31)
```

Instead, we can use the stdlib's
[`calendar.monthrange`](https://docs.python.org/3/library/calendar.html#calendar.monthrange):

```python
import calendar
import datetime as dt

last_day = calendar.monthrange(year, month)[1]
# 31
last = dt.date(year, month, last_day)
# datetime.date(2025, 12, 31)
```

## Three

Finally, to get last month as a yyyy-mm string:

```python
import datetime as dt

from dateutil.relativedelta import relativedelta

today = dt.date.today()
# datetime.date(2025, 12, 29)
d = today - relativedelta(months=1)
# datetime.date(2025, 11, 29)
d.isoformat()[:7]
# '2025-11'
```

Instead:

```python
import datetime as dt

today = dt.date.today()
# datetime.date(2025, 12, 29)
if today.month == 1:
    year, month = today.year - 1, 12
else:
    year, month = today.year, today.month - 1
    # 2025, 11
f"{year}-{month:02d}"
# '2025-11'
```

Goodbye six, and we also get slightly quicker install, import and run times.

## Bonus

I recommend
[Adam Johnson's tip](https://adamj.eu/tech/2019/09/12/how-i-import-pythons-datetime-module/)
to `import datetime as dt` to avoid the ambiguity of which `datetime` is the module and
which is the class.

---

<small>Header photo:
[Ver Sacrum calendar](https://archive.org/details/lfaaustria0001/LFA_Austria_0001_016.jpg)
by [Alfred Roller](https://www.museumoo.com/Libri/Ver-Sacrum-Kalender)</small>
