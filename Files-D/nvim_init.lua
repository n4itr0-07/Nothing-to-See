-- ~/.config/nvim/init.lua

-- Setup lazy.nvim
local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not vim.loop.fs_stat(lazypath) then
  vim.fn.system({
    "git", "clone", "--filter=blob:none",
    "https://github.com/folke/lazy.nvim.git",
    lazypath,
  })
end
vim.opt.rtp:prepend(lazypath)

-- Plugins
require("lazy").setup({
  { "folke/tokyonight.nvim", lazy = false, priority = 1000 },
  { "nvim-treesitter/nvim-treesitter", build = ":TSUpdate" },
})

-- Theme and Core
require("theme")
require("core") -- if exists
