#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Aliaksei Shytkin
# Copyright (c) 2015 Aliaksei Shytkin
#
# License: MIT
#

"""This module exports the mdl plugin class."""

from SublimeLinter.lint import RubyLinter


class Mdl(RubyLinter):

    """Provides an interface to mdl."""

    syntax = ('markdown', 'markdown gfm', 'multimarkdown')
    executable = 'mdl'
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 0.2.1'
    regex = r'^.+?:(?P<line>\d+): (?P<warning>(?P<message>[^`]*))'
    config_file = ('--config', '.mdlrc', '~')
    line_col_base = (1, 1)
    tempfile_suffix = 'md'
    inline_overrides = ('bundle-exec')

    def cmd(self):
        """Support bundle-exec."""

        if self.get_view_settings().get('bundle-exec', False):
            return ('bundle', 'exec', self.executable)
        return (self.executable_path)
