---
title: '💭 aca/emmet-ls: Emmet support based on LSP.'
date: 2023-09-08T12:34:38
templateKey: link
link: https://github.com/aca/emmet-ls
tags:
  - webdev
  - nvim
published: true

---

> This is the greatest nvim emmet plugin I have tried.  In the past I had tried the vim plugin a few times and just could not get a good flow with the keybindings and found it confusing for my occasional use.  `emmet-ls` just uses lsp-completion, so its the same flow as other completions.

You can try it out by installing with `:Mason`

## config

``` lua
local lspconfig = require('lspconfig')
local configs = require('lspconfig/configs')
local capabilities = vim.lsp.protocol.make_client_capabilities()
capabilities.textDocument.completion.completionItem.snippetSupport = true

lspconfig.emmet_ls.setup({
    -- on_attach = on_attach,
    capabilities = capabilities,
    filetypes = { "css", "eruby", "html", "javascript", "javascriptreact", "less", "sass", "scss", "svelte", "pug", "typescriptreact", "vue" },
    init_options = {
      html = {
        options = {
          -- For possible options, see: https://github.com/emmetio/emmet/blob/master/src/config.ts#L79-L267
          ["bem.enabled"] = true,
        },
      },
    }
})
```

[Original thought](https://github.com/aca/emmet-ls)
