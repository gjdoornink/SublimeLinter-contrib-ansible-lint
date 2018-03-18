#
# linter.py
# Linter for SublimeLinter4, a code checking framework for Sublime Text 3
#
# Written by Markus Liljedahl
# Copyright (c) 2017 Markus Liljedahl
#
# License: MIT
#

"""This module exports the AnsibleLint plugin class."""

from SublimeLinter.lint import Linter, util


class AnsibleLint(Linter):
    """Provides an interface to ansible-lint."""

    # ansbile-lint verison requirements check
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 3.0.1'

    # linter settings
    cmd = ('ansible-lint', '${args}', '@')
    regex = r'^.+:(?P<line>\d+): \[.(?P<error>.+)\] (?P<message>.+)'
    # -p generate non-multi-line, pep8 compatible output
    multiline = False

    # ansible-lint does not support column number
    word_re = False
    line_col_base = (1, 1)

    tempfile_suffix = 'yml'
    error_stream = util.STREAM_STDOUT

    defaults = {
        'selector': 'source.ansible',
        'args': '--nocolor -p',
        '--exclude= +': ['.galaxy'],
    }
    inline_overrides = ['exclude']
