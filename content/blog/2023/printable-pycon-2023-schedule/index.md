---
title: "Printable PyCon 2023 schedule"
date: "2023-04-15T10:10:02.541Z"
tags: ["pycon", "python", "print", "css"]
---

Want to print out the PyCon US 2023 schedule? Paper doesn't run out of batteries, is
easy to scribble on, and stuff into a pocket.

![Printed PyCons schedule](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/2mjm7whei9m178ljcrhx.jpg)

Here's some custom CSS and JavaScript to make it nicely printable.

1. Install the
   [Styler browser extension](https://chrome.google.com/webstore/detail/styler/bogdgcfoocbajfkjjolkmcdcnnellpkb?hl=en)

2. View a PyCon schedule page such as https://us.pycon.org/2023/schedule/talks/ and
   click the Styler extension's S icon

3. Paste this CSS into the upper box:

```CSS
body.pycon-schedule aside.sidebar,
body.pycon-schedule div.badges,
body.pycon-schedule button.menu-button.open-menu,
body.pycon-schedule button#theme-switch,
body.pycon-schedule footer {
  display: none;
}
body.pycon-schedule {
  font-size: 14px;
}
body.pycon-schedule main {
  padding: 0 !important;
}
body.pycon-schedule .calendar {
	left: auto !important;
  width: 100% !important;
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
    window.location.pathname.match("2023/schedule/") &&
    !window.location.pathname.match("2023/schedule/presentation/")
  ) {
    $("body").addClass("pycon-schedule");
  }
});
```

5. Print!

It'll run on any of the `https://us.pycon.org/2023/schedule/*` pages, but not the
individual presentation pages such as
`https://us.pycon.org/2023/schedule/presentation/88/`

Once printed, you can click the Styler icon and the `x` button to disable Styler for the
site so you can browse the original version.

![Printed PyCons schedule](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/59l815p02j0yk0jy377c.jpg)
