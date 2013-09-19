
from nose.plugins.base import Plugin


__version__ = '0.2'


class IgnoreDocstrings(Plugin):
    """
    Don't use docstrings to name tests.
    """

    name = 'ignore-docstrings'

    def describeTest(self, test):
        return str(test)
