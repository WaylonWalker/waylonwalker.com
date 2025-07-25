---
date: 2025-07-17 19:45:19
templateKey: til
title: pygments htmlformatter
published: true
tags:
  - python

---

I've been a long user of pygments, it's been the thing that injects `<spans>`
with funny little class names like `sc` and `si` into the code blocks of my
website.  I've even gone as far as implementing a [plugin for
md-it](https://github.com/WaylonWalker/markata/blob/main/markata/plugins/md_it_highlight_code.py),
but I had no idea how to re-style it.  I long ago got a theme that looked good
enough from somewhere and just used it, maybe I pulled something from their
docs site and forgot.  Today I learned you can list all the themes easily from
the library itself, and render out new css.

``` python
from pygments.styles import get_all_styles
list(get_all_styles())
# [
#     'abap',
#     'algol_nu',
#     'algol',
#     'arduino',
#     'autumn',
#     'borland',
#     'bw',
#     'colorful',
#     'default',
#     'dracula',
#     'emacs',
#     'friendly_grayscale',
#     'friendly',
#     'fruity',
#     'github-dark',
#     'gruvbox-dark',
#     'gruvbox-light',
#     'igor',
#     'inkpot',
#     'lightbulb',
#     'lilypond',
#     'lovelace',
#     'manni',
#     'material',
#     'monokai',
#     'murphy',
#     'native',
#     'nord-darker',
#     'nord',
#     'one-dark',
#     'paraiso-dark',
#     'paraiso-light',
#     'pastie',
#     'perldoc',
#     'rainbow_dash',
#     'rrt',
#     'sas',
#     'solarized-dark',
#     'solarized-light',
#     'staroffice',
#     'stata-dark',
#     'stata-light',
#     'stata',
#     'tango',
#     'trac',
#     'vim',
#     'vs',
#     'xcode',
#     'zenburn'
# ]
```

``` python
from pygments.formatters import HtmlFormatter
from pygments.styles import get_style_by_name
style = get_style_by_name("monokai")
formatter = HtmlFormatter(style=style)
print(formatter.get_style_defs('.highlight'))
```

And now you get styles that you can add to your css and be any theme from the
list above.

``` css
pre { line-height: 125%; }
td.linenos .normal { color: inherit; background-color: transparent; padding-left: 5px; padding-right: 5px; }
span.linenos { color: inherit; background-color: transparent; padding-left: 5px; padding-right: 5px; }
td.linenos .special { color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
span.linenos.special { color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
.highlight .hll { background-color: #49483e }
.highlight { background: #272822; color: #f8f8f2 }
.highlight .c { color: #959077 } /* Comment */
.highlight .err { color: #ed007e; background-color: #1e0010 } /* Error */
.highlight .esc { color: #f8f8f2 } /* Escape */
.highlight .g { color: #f8f8f2 } /* Generic */
.highlight .k { color: #66d9ef } /* Keyword */
.highlight .l { color: #ae81ff } /* Literal */
.highlight .n { color: #f8f8f2 } /* Name */
.highlight .o { color: #ff4689 } /* Operator */
.highlight .x { color: #f8f8f2 } /* Other */
.highlight .p { color: #f8f8f2 } /* Punctuation */
.highlight .ch { color: #959077 } /* Comment.Hashbang */
.highlight .cm { color: #959077 } /* Comment.Multiline */
.highlight .cp { color: #959077 } /* Comment.Preproc */
.highlight .cpf { color: #959077 } /* Comment.PreprocFile */
.highlight .c1 { color: #959077 } /* Comment.Single */
.highlight .cs { color: #959077 } /* Comment.Special */
.highlight .gd { color: #ff4689 } /* Generic.Deleted */
.highlight .ge { color: #f8f8f2; font-style: italic } /* Generic.Emph */
.highlight .ges { color: #f8f8f2; font-weight: bold; font-style: italic } /* Generic.EmphStrong */
.highlight .gr { color: #f8f8f2 } /* Generic.Error */
.highlight .gh { color: #f8f8f2 } /* Generic.Heading */
.highlight .gi { color: #a6e22e } /* Generic.Inserted */
.highlight .go { color: #66d9ef } /* Generic.Output */
.highlight .gp { color: #ff4689; font-weight: bold } /* Generic.Prompt */
.highlight .gs { color: #f8f8f2; font-weight: bold } /* Generic.Strong */
.highlight .gu { color: #959077 } /* Generic.Subheading */
.highlight .gt { color: #f8f8f2 } /* Generic.Traceback */
.highlight .kc { color: #66d9ef } /* Keyword.Constant */
.highlight .kd { color: #66d9ef } /* Keyword.Declaration */
.highlight .kn { color: #ff4689 } /* Keyword.Namespace */
.highlight .kp { color: #66d9ef } /* Keyword.Pseudo */
.highlight .kr { color: #66d9ef } /* Keyword.Reserved */
.highlight .kt { color: #66d9ef } /* Keyword.Type */
.highlight .ld { color: #e6db74 } /* Literal.Date */
.highlight .m { color: #ae81ff } /* Literal.Number */
.highlight .s { color: #e6db74 } /* Literal.String */
.highlight .na { color: #a6e22e } /* Name.Attribute */
.highlight .nb { color: #f8f8f2 } /* Name.Builtin */
.highlight .nc { color: #a6e22e } /* Name.Class */
.highlight .no { color: #66d9ef } /* Name.Constant */
.highlight .nd { color: #a6e22e } /* Name.Decorator */
.highlight .ni { color: #f8f8f2 } /* Name.Entity */
.highlight .ne { color: #a6e22e } /* Name.Exception */
.highlight .nf { color: #a6e22e } /* Name.Function */
.highlight .nl { color: #f8f8f2 } /* Name.Label */
.highlight .nn { color: #f8f8f2 } /* Name.Namespace */
.highlight .nx { color: #a6e22e } /* Name.Other */
.highlight .py { color: #f8f8f2 } /* Name.Property */
.highlight .nt { color: #ff4689 } /* Name.Tag */
.highlight .nv { color: #f8f8f2 } /* Name.Variable */
.highlight .ow { color: #ff4689 } /* Operator.Word */
.highlight .pm { color: #f8f8f2 } /* Punctuation.Marker */
.highlight .w { color: #f8f8f2 } /* Text.Whitespace */
.highlight .mb { color: #ae81ff } /* Literal.Number.Bin */
.highlight .mf { color: #ae81ff } /* Literal.Number.Float */
.highlight .mh { color: #ae81ff } /* Literal.Number.Hex */
.highlight .mi { color: #ae81ff } /* Literal.Number.Integer */
.highlight .mo { color: #ae81ff } /* Literal.Number.Oct */
.highlight .sa { color: #e6db74 } /* Literal.String.Affix */
.highlight .sb { color: #e6db74 } /* Literal.String.Backtick */
.highlight .sc { color: #e6db74 } /* Literal.String.Char */
.highlight .dl { color: #e6db74 } /* Literal.String.Delimiter */
.highlight .sd { color: #e6db74 } /* Literal.String.Doc */
.highlight .s2 { color: #e6db74 } /* Literal.String.Double */
.highlight .se { color: #ae81ff } /* Literal.String.Escape */
.highlight .sh { color: #e6db74 } /* Literal.String.Heredoc */
.highlight .si { color: #e6db74 } /* Literal.String.Interpol */
.highlight .sx { color: #e6db74 } /* Literal.String.Other */
.highlight .sr { color: #e6db74 } /* Literal.String.Regex */
.highlight .s1 { color: #e6db74 } /* Literal.String.Single */
.highlight .ss { color: #e6db74 } /* Literal.String.Symbol */
.highlight .bp { color: #f8f8f2 } /* Name.Builtin.Pseudo */
.highlight .fm { color: #a6e22e } /* Name.Function.Magic */
.highlight .vc { color: #f8f8f2 } /* Name.Variable.Class */
.highlight .vg { color: #f8f8f2 } /* Name.Variable.Global */
.highlight .vi { color: #f8f8f2 } /* Name.Variable.Instance */
.highlight .vm { color: #f8f8f2 } /* Name.Variable.Magic */
.highlight .il { color: #ae81ff } /* Literal.Number.Integer.Long */
```
