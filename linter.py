#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by roadhump
# Copyright (c) 2015 roadhump
#
# License: MIT
#

"""This module exports the Mdl plugin class."""

from SublimeLinter.lint import RubyLinter, util


class Mdl(RubyLinter):

    """Provides an interface to mdl."""

    syntax = ('markdown')
    executable = 'mdl'
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 0.2.1'
    regex = r'^.+?:(?P<line>\d+): (?P<message>[^`]*)'
    # multiline = True
    line_col_base = (1, 1)
    tempfile_suffix = 'md'
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = r'\s*#'

    def cmd(self):
            if self.get_view_settings().get('bundle-exec', False):
                return ('bundle', 'exec', self.executable)
            return (self.executable_path)

