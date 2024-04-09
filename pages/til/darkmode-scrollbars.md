---
date: 2024-04-10 11:56:38
templateKey: til
title: darkmode scrollbars
published: true
tags:
  - webdev

---

If you are designing a website in dark mode the scrollbars can be finicky to
match the theme.  Here is a pretty sane default that looks nice without being
obnoxiously contrast to the rest of the site.

``` html
    <style>
        ::-webkit-scrollbar {
            height: 1rem;
            width: 1rem;
        }

        ::-webkit-scrollbar-track {
            background-color: rgb(24 24 27);
        }

        body::-webkit-scrollbar-track {
            background-color: rgb(39 39 42);
        }

        ::-webkit-scrollbar-thumb {
            background-color: rgb(82 82 91);
        }

        ::-webkit-scrollbar-thumb:hover {
            background-color: rgb(113 113 122);
        }

        body::-webkit-scrollbar-thumb {
            background-color: rgb(82 82 91);
        }

        body::-webkit-scrollbar-thumb:hover {
            background-color: rgb(113 113 122);
        }

        ::-webkit-scrollbar-corner {
            background-color: rgb(39 39 42);
        }
    </style>
```

Want a rounded scrollbar thumb? add these styles.

``` css
::-webkit-scrollbar-thumb {
    border-radius: 0.25rem;
    border-radius: 9999px;
}

body::-webkit-scrollbar-thumb {
    border-radius: 0.25rem;
    border-radius: 9999px;
}
```

This makes a very nice looking default darkmode scrollbar.
