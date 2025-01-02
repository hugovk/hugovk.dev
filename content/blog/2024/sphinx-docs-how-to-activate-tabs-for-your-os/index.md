---
title: "Sphinx docs: How to activate tabs for your OS"
date: "2024-04-02T18:41:30.300Z"
tags: ["python", "documentation", "sphinx", "javascript"]
---

On the [Python Developer's Guide](https://devguide.python.org/) and
[Pillow documentation](https://pillow.readthedocs.io/en/latest/installation/basic-installation.html)
we have some pages with tabs for different operating systems:

![Screenshot showing instructions how to build Python. Some parts have Unix, macOS and Windows tabs. The macOS tab is active, showing a configure command to run in your terminal. Underneath is a second step with its own tabs and a macOS command. There's a macOS-specific note underneath.](knze2ghlj0qmjucz354t.png)

It's possible to add some JavaScript so that the matching tab is activated based on the
visitor's operating system.

Here's how!

## Sphinx Inline Tabs

First add the [Sphinx Inline Tabs](https://github.com/pradyunsg/sphinx-inline-tabs)
extension to your docs'
[`requirements.txt`](https://github.com/python/devguide/blob/d92fda3beb5506eb42d53fee1c52d31180e9d77a/requirements.txt#L4):

```txt
# requirements.txt
sphinx-inline-tabs>=2023.4.21
```

# JavaScript

Next, add
[`activate_tab.js`](https://github.com/python/devguide/blob/d92fda3beb5506eb42d53fee1c52d31180e9d77a/_static/activate_tab.js)
to your `_static/` directory:

```js
// activate_tab.js
// Based on https://stackoverflow.com/a/38241481/724176
function getOS() {
  const userAgent = window.navigator.userAgent,
    platform = window.navigator?.userAgentData?.platform || window.navigator.platform,
    macosPlatforms = ["macOS", "Macintosh", "MacIntel", "MacPPC", "Mac68K"],
    windowsPlatforms = ["Win32", "Win64", "Windows", "WinCE"],
    iosPlatforms = ["iPhone", "iPad", "iPod"];

  if (macosPlatforms.includes(platform)) {
    return "macOS";
  } else if (iosPlatforms.includes(platform)) {
    return "iOS";
  } else if (windowsPlatforms.includes(platform)) {
    return "Windows";
  } else if (/Android/.test(userAgent)) {
    return "Android";
  } else if (/Linux/.test(platform)) {
    return "Unix";
  }

  return "unknown";
}

function activateTab(tabName) {
  // Find all label elements containing the specified tab name
  const labels = document.querySelectorAll(".tab-label");

  labels.forEach((label) => {
    if (label.textContent.includes(tabName)) {
      // Find the associated input element using the 'for' attribute
      const tabInputId = label.getAttribute("for");
      const tabInput = document.getElementById(tabInputId);

      // Check if the input element exists before attempting to set the "checked" attribute
      if (tabInput) {
        // Activate the tab by setting its "checked" attribute to true
        tabInput.checked = true;
      }
    }
  });
}
```

# `conf.py`

Add the
[extension](https://github.com/python/devguide/blob/d92fda3beb5506eb42d53fee1c52d31180e9d77a/conf.py#L15)
and
[JavaScript](https://github.com/python/devguide/blob/d92fda3beb5506eb42d53fee1c52d31180e9d77a/conf.py#L49-L51)
to your `conf.py`:

```python
# conf.py
extensions = [
    "sphinx_inline_tabs",
]

html_js_files = [
    "activate_tab.js",
]
```

## reStructuredText

Almost there!

Add tabs to the reStructuredText files.

For
[example](https://github.com/python/devguide/blob/d92fda3beb5506eb42d53fee1c52d31180e9d77a/testing/run-write-tests.rst#L58-L74),
here we have three different commands; one for Unix, one for macOS, and one for Windows:

```reStructuredText
.. tab:: Unix

    .. code-block:: shell

        ./python -m test -h

.. tab:: macOS

    .. code-block:: shell

        ./python.exe -m test -h

.. tab:: Windows

    .. code-block:: dosbatch

        .\python.bat -m test -h
```

Finally, add the JavaScript
[to the same reST page](https://github.com/python/devguide/blob/d92fda3beb5506eb42d53fee1c52d31180e9d77a/testing/run-write-tests.rst#L8-L14)
to activate the correct tab:

```rst
.. raw:: html

    <script>
    document.addEventListener('DOMContentLoaded', function() {
      activateTab(getOS());
    });
    </script>
```

You can see the results
[here](https://devguide.python.org/testing/run-write-tests/#running). When the page
loads, the browser finds the browser name, and activates the tabs with a matching name.

If you have many sets of tabs on a page, the corresponding OS tab will be activated for
all. And if you click on another OS tab, all the others with the same name are
activated.

Happy tabbing!

---

<small>Header photo:
"<a target="_blank" rel="noopener noreferrer" href="https://www.flickr.com/photos/nationalgalleries/3110282571/">The
Great Pyramid and the Sphinx</a>" by
<a target="_blank" rel="noopener noreferrer" href="https://www.flickr.com/photos/nationalgalleries/">National
Galleries of Scotland</a>, with
<a target="_blank" rel="noopener noreferrer" href="https://www.flickr.com/commons/usage/">no
known copyright restrictions</a>.</small>
