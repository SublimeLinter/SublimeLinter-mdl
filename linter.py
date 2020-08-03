from SublimeLinter.lint import Linter


class RubyLinter(Linter):
    def context_sensitive_executable_path(self, cmd):
        # The default implementation will look for a user defined `executable`
        # setting.
        success, executable = super().context_sensitive_executable_path(cmd)
        if success:
            return True, executable

        gem_name = cmd[0] if isinstance(cmd, list) else cmd

        if self.settings.get('use_bundle_exec', False):
            return True, ['bundle', 'exec', gem_name]

        rvm = self.which('rvm-auto-ruby')
        if rvm:
            return True, [rvm, '-S', gem_name]

        return False, None


class Mdl(RubyLinter):
    cmd = ['mdl', '${temp_file}']
    regex = r'^.+?:(?P<line>\d+): (?P<warning>(?P<message>[^`]*))'
    line_col_base = (1, 1)
    tempfile_suffix = 'md'
    defaults = {
        'selector': 'text.html.markdown'
    }
