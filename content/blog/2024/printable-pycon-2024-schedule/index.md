---
title: "Printable PyCon 2024 schedule"
date: "2024-05-11T11:01:33.935Z"
tags: ["pycon", "python", "print", "css"]
---

Want to print out the PyCon US schedule? Paper doesn't run out of batteries, is easy to
scribble on, and stuff into a pocket (technical term: _the affordances of paper_).

Here's some custom CSS and JavaScript to make it nicely printable.

1. Install the
   [Styler browser extension](https://chrome.google.com/webstore/detail/styler/bogdgcfoocbajfkjjolkmcdcnnellpkb?hl=en)

2. View a PyCon schedule page such as https://us.pycon.org/2024/schedule/talks/ and
   click the Styler extension's S icon

3. Paste this CSS into the upper box:

```CSS
body.pycon-schedule div.internal-page-header,
body.pycon-schedule div.panel-heading,
body.pycon-schedule footer,
body.pycon-schedule div.badges {
  display: none;
}

body.pycon-schedule .container {
  margin: 0;
  max-width: fit-content;
}
body.pycon-schedule main.content {
  margin: 0;
  width: 100% !important;
}
body.pycon-schedule .calendar {
  left: auto !important;
  width: 100% !important;
}
body.pycon-schedule .slot {
  padding: 5px;
}
@media print {
  a:after { content:''; }
  a[href]:after { content: none !important; }
}
```

4. Paste this JavaScript into the lower box:

```js
$(document).ready(function () {
  if (
    window.location.pathname.match("2024/schedule/") &&
    !window.location.pathname.match("2024/schedule/presentation/")
  ) {
    $("body").addClass("pycon-schedule");
  }
});
```

5. Print!

It'll run on any of the `https://us.pycon.org/2024/schedule/*` pages, but not the
individual presentation pages such as
`https://us.pycon.org/2024/schedule/presentation/61/`

It's not perfect, the right edge is slightly cut off, but it's more printable than the
original.

Once printed, you can click the Styler icon and the `x` button to disable Styler for the
site so you can browse the original version.

See also:

- [Printable PyCon 2023 schedule](../2023/printable-pycon-2023-schedule)
