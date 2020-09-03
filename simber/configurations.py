"""File to handle the default configurations
of the logger."""


class Default(object):
    """Store all default fields that are
    necessary for proper functioning of the
    logger.

    None of the attributes will be exposed
    directly, each of them will be read only.

    The name of the attribute should start with an
    underscore and the attribute method should be
    the same without an underscore.
    """
    def __init__(self):
        self._console_format = ""
        self._file_format = ""

    @property
    def console_format(self) -> str:
        return self._console_format

    @property
    def file_format(self) -> str:
        return self._file_format

    def __repr__(self) -> str:
        """Return a string showing all the attributes
        that self contains"""
        return str({
            'console_format': self.console_format(),
            'file_format': self.file_format()
        })
