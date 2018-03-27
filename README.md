# SublimeLinter-mdl

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-mdl.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-mdl)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [Markdown lint tool (mdl)](https://github.com/mivok/markdownlint). It will be used with files that have the “Markdown” syntax.


## Installation
SublimeLinter 3 must be installed in order to use this plugin. 

Please install via [Package Control](https://sublime.wbond.net/installation).

Before using this plugin, you must ensure that `mdl` is installed on your system. To install `mdl`, do the following:

1. Install [Ruby](http://www.ruby-lang.org).

1. Install `mdl` by typing the following in a terminal:

   ```
   [sudo] gem install mdl
   ```

1. If you are using `rbenv` or `rvm`, ensure that they are loaded in your shell’s correct startup file. See [here](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#shell-startup-files) for more information.


## Settings

- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html

Additional SublimeLinter-mdl settings:

|Setting|Description|
|:------|:----------|
|bundle-exec|runs mdl as "bundle exec mdl" instead of "mdl"|
