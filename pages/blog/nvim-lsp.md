---
templateKey: blog-post
tags: ['vim', 'linux', 'python']
title: python lsp setup
date: 2021-05-17T16:13:42
status: draft

---

Setting up python with the native nvim>0.5 lsp was mr


## lsp-config

https://github.com/neovim/nvim-lspconfig

``` vim
lua << EOF
require'lspconfig'.pyright.setup{}
EOF
```

## pyls#190

https://github.com/palantir/python-language-server/issues/190

``` lua
lspconfig.pyls.setup {
  cmd = {"pyls"},
  filetypes = {"python"},
  settings = {
    pyls = {
      configurationSources = {"flake8"},
      plugins = {
        jedi_completion = {enabled = true},
        jedi_hover = {enabled = true},
        jedi_references = {enabled = true},
        jedi_signature_help = {enabled = true},
        jedi_symbols = {enabled = true, all_scopes = true},
        pycodestyle = {enabled = false},
        flake8 = {
          enabled = true,
          ignore = {},
          maxLineLength = 160
        },
        mypy = {enabled = false},
        isort = {enabled = false},
        yapf = {enabled = false},
        pylint = {enabled = false},
        pydocstyle = {enabled = false},
        mccabe = {enabled = false},
        preload = {enabled = false},
        rope_completion = {enabled = false}
      }
    }
  },
  on_attach = on_attach
}
```


## mypy

Getting mypy working with lsp was tricky for me.  I had some issues trying to
run mypy in ci and pyright in my editor and I really wanted them to match.

``` bash
pipx install 'python-lsp-server[all]'
pipx inject python-lsp-server pylsp-mypy
```


