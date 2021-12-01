---
templateKey: blog-post
tags: ['linux', 'vim', 'neovim']
title: Setup a yaml schema | yamlls for a silky smooth setup
date: 2021-11-30T23:24:52
status: draft

---

https://youtu.be/9B_P19O0MPw

## init.vim

``` vim
source ~/.config/nvim/plugins.vim
lua require'waylonwalker.cmp'
lua require'waylonwalker.lsp-config'
```

## Plugin setup

``` vim
" /home/u_walkews/.config/nvim/plugins.vim
Plug 'neovim/nvim-lspconfig'

" if you want to use nvim-cmp
Plug 'hrsh7th/nvim-cmp'
Plug 'hrsh7th/cmp-nvim-lsp'

" if you want to use lsp-install
Plug 'kabouzeid/nvim-lspinstall'
```

## cmp config

Make sure that you have nvim_lsp as a source in your cmp config.

``` lua
--  ~/.config/nvim/lua/waylonwalker/lsp-config.lua
-- Setup nvim-cmp.
local cmp = require'cmp'

cmp.setup({
snippet = {
    expand = function(args)
    -- For `vsnip` user.
    vim.fn["vsnip#anonymous"](args.body)

    -- For `luasnip` user.
    -- require('luasnip').lsp_expand(args.body)

    -- For `ultisnips` user.
    -- vim.fn["UltiSnips#Anon"](args.body)
    end,
},
mapping = {
  ['<C-n>'] = cmp.mapping.select_next_item({ behavior = cmp.SelectBehavior.Insert }),
  ['<C-p>'] = cmp.mapping.select_prev_item({ behavior = cmp.SelectBehavior.Insert }),
  ['<Down>'] = cmp.mapping.select_next_item({ behavior = cmp.SelectBehavior.Select }),
  ['<Up>'] = cmp.mapping.select_prev_item({ behavior = cmp.SelectBehavior.Select }),
  ['<C-d>'] = cmp.mapping.scroll_docs(-4),
  ['<C-f>'] = cmp.mapping.scroll_docs(4),
  ['<C-Space>'] = cmp.mapping.complete(),
  ['<C-e>'] = cmp.mapping.close(),
  ['<CR>'] = cmp.mapping.confirm({
    behavior = cmp.ConfirmBehavior.Replace,
    select = true,
    })
},
sources = {
    { name = 'nvim_lsp' },
    { name = 'vsnip' },
    { name = 'path' },
    { name = 'buffer' },
    { name = 'calc' },
    { name = 'tmux' },
}
})

```

## lsp config



``` lua
--  ~/.config/nvim/lua/waylonwalker/lsp-config.lua
require'lspconfig'.yamlls.setup{
    on_attach=on_attach,
    capabilities = require('cmp_nvim_lsp').update_capabilities(vim.lsp.protocol.make_client_capabilities()),
    settings = {
        yaml = {
            schemas = {
                ["https://raw.githubusercontent.com/quantumblacklabs/kedro/develop/static/jsonschema/kedro-catalog-0.17.json"]= "conf/**/*catalog*",
                ["https://json.schemastore.org/github-workflow.json"] = "/.github/workflows/*"
            }
        }
    }
}
```

## Related Links

* [my nvim config](https://github.com/WaylonWalker/devtainer/tree/main/nvim/.config/nvim)
* [nvim-lspconfig GitHub]( https://github.com/neovim/nvim-lspconfig )
* [nvim-cmp GitHub]( https://github.com/hrsh7th/nvim-cmp )
* [lspinstall yamlls]( https://github.com/kabouzeid/nvim-lspinstall/blob/main/lua/lspinstall/servers/yaml.lua )
* [yaml-language-server npm]( https://www.npmjs.com/package/yaml-language-server?activeTab=readme )
