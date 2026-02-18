# /// script
# requires-python = ">=3.10"
# dependencies = ["pyperclip"]
# ///

import datetime as dt

import pyperclip

timestamp = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
print(timestamp)
pyperclip.copy(timestamp)
