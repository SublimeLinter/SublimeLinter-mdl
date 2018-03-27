from SublimeLinter.lint import RubyLinter


class Mdl(RubyLinter):
    executable = 'mdl'
    regex = r'^.+?:(?P<line>\d+): (?P<warning>(?P<message>[^`]*))'
    line_col_base = (1, 1)
    tempfile_suffix = 'md'
    defaults = {
        'selector': 'text.html.markdown'
    }

    def cmd(self):
        """Support bundle-exec."""

        if self.get_view_settings().get('bundle-exec', False):
            return ('bundle', 'exec', self.executable)
        return (self.executable_path)
