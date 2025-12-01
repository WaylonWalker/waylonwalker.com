---
templateKey: blog-post
tags: ["linux", "vim", "neovim"]
title: Setup a yaml schema | yamlls for a silky smooth setup
date: 2021-12-03T23:24:52
published: true
---

I've gone far too long without a good setup for editing yaml
files, I am missing out on autocomplete and proper diagnostics.
This ends today as I setup yaml-language-server in neovim.

[https://youtu.be/xo4HrFoKF4c](https://youtu.be/xo4HrFoKF4c){.youtube-embed}

The video for this one is part of a
[challenge-playlist](https://www.youtube.com/playlist?list=PLTRNG6WIHETAj0nR_WYAxxGjd7kXch5zj)
I put out for myself to constantly improve my dotfiles for all of December.

## init.vim

I have my `init.vim` setup to only source other modules, if you want everything
in a single config, feel free to do as you wish. I broke mine up earlier this
year as I doubled into nvim and am not going back.

```vim
source ~/.config/nvim/plugins.vim
lua require'waylonwalker.cmp'
lua require'waylonwalker.lsp-config'
```

## Plugin setup

You will need the following plugins. I use plug, if you don't you will have to
convert the syntax over to the plugin manager you use.

[neovim/nvim-lspconfig](https://github.com/neovim/nvim-lspconfig) is for
configuring the lsp. It comes with a bunch of sane defaults for most servers,
so you pretty much just have to call setup on that server unless you want to
change the defaults.

[hrsh7th/nvim-cmp](https://github.com/hrsh7th/nvim-cmp) is what I use for
autocomplete. If you are using something else you might need to set that up in
a different way in order to get the autocomplete to work. You will still get
the diagnostics with just lsp-config.

[kabouzeid/nvim-lspinstall](https://github.com/kabouzeid/nvim-lspinstall) will
aide in installing lsp's if you want. I have chosen not to because I want to
have my full setup scripted so when I setup any new machine I just run my
ansible-playbook. This library is nice to just set things up quick and play
with them.

```vim
" /home/u_walkews/.config/nvim/plugins.vim
Plug 'neovim/nvim-lspconfig'

" if you want to use nvim-cmp
Plug 'hrsh7th/nvim-cmp'
Plug 'hrsh7th/cmp-nvim-lsp'

" if you want to use lsp-install
Plug 'kabouzeid/nvim-lspinstall'
```

## cmp config

Make sure that you have nvim_lsp as a source in your cmp config. This is my
config as of now, its likely to change in the future, set yours up how you
like. hrsh7th has a really good readme if you want help configuring cmp.

> Again if you don't use cmp you can skip this step, cmp is for autocomplete.
> You can use a different plugin for autocomplete, or not use a plugin at all
> if that's your thing.

```lua
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

Next up is the heart of this post, the lsp-config.lua. This one is pretty
straight forward, require lspconfig (which you need the plugin for), then set
it up with cmp and the extra schemas. I'm sure there are yaml schemas for tons
of things, I'll probably add more in the future, but for now, this is what I
have.

```lua
--  ~/.config/nvim/lua/waylonwalker/lsp-config.lua
require'lspconfig'.yamlls.setup{
    on_attach=on_attach,
    capabilities = require('cmp_nvim_lsp').update_capabilities(vim.lsp.protocol.make_client_capabilities()),
    settings = {
        yaml = {
            schemas = {
                ["https://raw.githubusercontent.com/kedro-org/kedro/develop/static/jsonschema/kedro-catalog-0.17.json"]= "conf/**/*catalog*",
                ["https://json.schemastore.org/github-workflow.json"] = "/.github/workflows/*"
            }
        }
    }
}
```

## Related Links

- [my nvim config](https://github.com/WaylonWalker/devtainer/tree/main/nvim/.config/nvim)
- [nvim-lspconfig GitHub](https://github.com/neovim/nvim-lspconfig)
- [nvim-cmp GitHub](https://github.com/hrsh7th/nvim-cmp)
- [lspinstall yamlls](https://github.com/kabouzeid/nvim-lspinstall/blob/main/lua/lspinstall/servers/yaml.lua)
- [yaml-language-server npm](https://www.npmjs.com/package/yaml-language-server?activeTab=readme)

Follow the [YouTube channel](https://youtube.com/waylonwalker) or the
[rss-feed](https://waylonwalker/rss/) to stay up to date.

## Also Check out My python lsp setup

[https://waylonwalker.com/setup-pylsp/](https://waylonwalker.com/setup-pylsp/){.hoverlink}
