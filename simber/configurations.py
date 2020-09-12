"""File to handle the default configurations
of the logger."""

from typing import Dict, List


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
        self._console_format = "%a[{levelname}]% [{logger}]"
        self._file_format = "[{levelname}] [{time}] [{filename}]"
        self._log_file_name = "log"
        self._valid_stdout_names = ['<stdout>', '<stderr>']
        self._level_number = {
            "DEBUG": 0,
            "INFO": 1,
            "WARNING": 2,
            "ERROR": 3,
            "CRITICAL": 4,
        }
        self._color_level_map = {
            "DEBUG": "b",
            "INFO": "g",
            "WARNING": "y",
            "ERROR": "r",
            "CRITICAL": "r"
        }

    @property
    def console_format(self) -> str:
        return self._console_format

    @property
    def file_format(self) -> str:
        return self._file_format

    @property
    def level_number(self) -> Dict:
        return self._level_number

    @property
    def log_file_name(self) -> str:
        return self._log_file_name

    @property
    def valid_stdout_names(self) -> List:
        return self._valid_stdout_names

    @property
    def color_level_map(self) -> Dict:
        return self._color_level_map

    def __repr__(self) -> str:
        """Return a string showing all the attributes
        that self contains"""
        return str({
            'console_format': self.console_format,
            'file_format': self.file_format,
            'level_number': self.level_number,
            'log_file_name': self.log_file_name,
            'valid_stdout_names': self.valid_stdout_names,
            'color_level_map': self.color_level_map
        })
