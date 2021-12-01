---
templateKey: blog-post
tags: ['linux', 'vim', 'neovim']
title: How linux users install a text editor
date: 2021-11-30T23:18:24
status: published

---


In honor of the neovim 0.6.0 release, I decided to do a funny skit installing
neovim, and fix up my install script in the process as part of my challenge to
fix up my dotfiles.  I ran into one snag where I was not updating the repo that
I cloned.  I moved it to the directory I now keep third-party git repos and set
it to update with ansible.

https://youtu.be/64oKLphhBuo

The thing that took me the longest to realize was.... I had a path issue
pointing me to an old install of the appimage over the fresh build,  fixed that
up and now we are on 0.7.0 nightly.


## Related Links

https://neovim.io/
https://github.com/neovim/neovim
https://github.com/neovim/neovim/releases/tag/v0.6.0
