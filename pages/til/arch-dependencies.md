---
date: 2024-04-20 07:42:21
templateKey: til
title: arch dependencies
published: true
tags:
  - linux
  - arch

---

paru has some nice features that I rarely use, and hav to look up when I need
them.  Here are two commands to help with dependency management.

``` bash
❯ paru -Qii nodejs
Name            : nodejs
Version         : 21.7.2-1
Description     : Evented I/O for V8 javascript
Architecture    : x86_64
URL             : https://nodejs.org/
Licenses        : MIT
Groups          : None
Provides        : None
Depends On      : icu  libuv  libnghttp2  libnghttp3  libngtcp2  openssl  zlib  brotli  c-ares
Optional Deps   : npm: nodejs package manager [installed]
Required By     : node-gyp  nodejs-nopt  npm  semver
Optional For    : None
Conflicts With  : None
Replaces        : None
Installed Size  : 46.86 MiB
Packager        : Felix Yan <felixonmars@archlinux.org>
Build Date      : Thu 04 Apr 2024 05:11:09 AM CDT
Install Date    : Mon 15 Apr 2024 07:27:02 AM CDT
Install Reason  : Installed as a dependency for another package
Install Script  : No
Validated By    : Signature
Backup Files    : None
Extended Data   : pkgtype=pkg
```

You can check all the packages depended on by nodejs by running the following.
This is everything from all of the repos you have configured, not what you have
installed.

``` bash
❯ pactree --reverse --sync --depth 1 nodejs

nodejs
├─acorn
├─ansible-language-server
├─asar
├─babel-cli
├─babel-core
├─bash-language-server
├─blinksocks
├─bower
├─browserify
├─coffeescript
├─dot-language-server
├─emscripten
├─eslint
├─eslint-language-server
├─eslint_d
├─gitlab
├─gnomon
├─grunt-cli
├─gtop
├─gulp
├─hedgedoc
├─jake
├─markdownlint-cli2
├─marked
├─marked-man
├─matrix-appservice-irc
├─modclean
├─node-gyp
├─nodejs-emojione
├─nodejs-material-design-icons
├─nodejs-nopt
├─nodejs-source-map
├─nodejs-yaml
├─npm
├─openui5
├─pm2
├─prettier
├─pyright
├─rapydscript-ng
├─s3rver
├─semver
├─serverless
├─stylelint
├─stylus
├─svelte-language-server
├─tailwindcss-language-server
├─ts-node
├─typescript
├─typescript-svelte-plugin
├─uglify-js
├─vscode-css-languageserver
├─vscode-html-languageserver
├─vscode-json-languageserver
├─vue-language-server
├─vue-typescript-plugin
├─wasm-bindgen
├─web-ext
├─wrangler
├─yaml-language-server
├─yarn
```
