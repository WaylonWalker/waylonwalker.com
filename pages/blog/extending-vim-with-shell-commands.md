---
date: 2022-11-12 18:38:11
templateKey: blog-post
title: extending vim with shell commands
tags:
  - vim
status: draft

---

Vimconf 2022

## The pitch

Extending vim does not need to be complicated and can be done using cli tools
that you might already be comfortable with.  Examples, setting up
codeformatters with autocmds, using lf/ranger as a tui file manager, generating
new files using a template framework like cookiecutter/copier/yeoman, using ag
to populate your quickfix.

## run a command

```
vimconf!!<esc>!!figlet
```

## formatters

``` lua
local settings = require'waylonwalker.settings'

M.waylonwalker_augroup = augroup('waylonwalker', { clear = true })
M.format_python = function()
    if settings.auto_format.python then
        vim.cmd('silent execute "%!tidy-imports --black --quiet --replace-star-imports --replace --add-missing --remove-unused " . bufname("%")')
        vim.cmd('silent execute "%!isort " . bufname("%")')
        vim.cmd('silent execute "%!black " . bufname("%")')
    end
end

autocmd({ "BufWritePost" }, {
    group=M.waylonwalker_augroup,
    pattern = { "*.py" },
    callback = M.format_python,
})
```

## File Navigation

``` lua
vim.keymap.set('n', 'geit', '<cmd>terminal markata list --map path --filter \'"til" in path\' --fast --no-pager<cr>')
```

``` lua
vim.keymap.set('n', 'geit', '<cmd>Telescope find_files find_command=markata,list,--map,path,--filter,date==today,--fast<cr>')
```

``` lua
vim.keymap.set('n', '<leader>ee', '<cmd>vertical terminal lf<cr>')
```

## FloatTerm

``` lua
vim.keymap.set('n', '<leader><leader>w', '<cmd>FloatermNew waylonwalker<cr>')
vim.g['floaterm_opener'] = 'vsplit'
vim.keymap.set('n', 'gee', '<cmd>FloatermNew lf<cr>')
```

## vimgrep over hidden files ##

I know all the files that I care to search for are called build.yml, and they
are in a hidden directory.

``` vim
:args `fd -H build.yml`
:vimgrep /upload docs/ ##
```

Once opened as a buffer by using args, and a handy fd command I can vimgrep
over all the open buffers using `##`

> Open buffers are represented by ##

Now I can just `dap` and `:cnext` my way through the list of changes that I
have, and know that I hit every one of them when I am at the end of my list.
And can double check this in about 10s by scrolling back through the quickfix
list.
