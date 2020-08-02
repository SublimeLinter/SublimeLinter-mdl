from SublimeLinter.lint import Linter


class Mdl(Linter):
    cmd= ['mdl', '${temp_file}']
    regex = r'^.+?:(?P<line>\d+): (?P<warning>(?P<message>[^`]*))'
    line_col_base = (1, 1)
    tempfile_suffix = 'md'
    defaults = {
        'selector': 'text.html.markdown'
    }

