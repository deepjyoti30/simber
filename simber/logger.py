"""A simple, minimal and powerful logger for Python.

It was merely built because of some restrictions that the
Python's default logging library has. This library is
aimed as a simple, minimal yet powerful logging library
for all Python apps.

Copyright (c) 2020 Deepjyoti Barman <deep.barman30@gmail.com>
"""
from pathlib import Path
import os

from simber.configurations import Default
from simber.formatter import Formatter


class Logger(object):
    """Handle the logging through one class. This will be the
    class exposed to the users.

    This class will have various methods but the most important
    methods are the ones that will allow the user to log at
    various levels.
    """

    _instances = []

    def __init__(
        self,
        name,
        format=None,
        file_format=None,
        log_path=None,
        level="INFO",
        disable_file=False,
        update_all=False
    ):
        self.name = name
        self._log_file = log_path
        self._level_number = Default().level_number
        self._passed_level = level
        self.level = self._level_number[level]
        self._disable_file = disable_file

        self._check_logfile()
        self._check_format(format, file_format)

        # Update all instances, if asked to
        if update_all:
            self.update_format(self._console_format, self._file_format)
            self.update_disable_file(self._disable_file)
            self.update_level(self.level)

        self._instances.append(self)

    def _check_format(self, format_passed, file_format):
        """Check the format that needs to be used.

        If the `format` passed is not None, use it.
        If the `file_format` is not None, use it, else
        use the `format` for the same.
        If `format` and `file_format` are not passed,
        use the default formats.
        """
        format_valid = bool(format_passed)
        file_format_valid = bool(file_format)

        if format_valid:
            if not file_format_valid:
                file_format = format_passed
            else:
                pass
        elif not format_valid:
            format_passed = Default().console_format
            if not file_format_valid:
                file_format = Default().file_format
            else:
                pass

        self._console_format = format_passed
        self._file_format = file_format

    def _check_logfile(self):
        """
        Check if the passed logfile path is present.
        If not present then create it.
        """
        # If the log_file path is not passed, disable the
        # logging to file
        if self._log_file is None:
            self._disable_file = True
            return

        # If it is passed, make it a Path object
        self._log_file = Path(self._log_file).expanduser()

        if not self._log_file.exists():
            if not self._log_file.parent.exists():
                os.makedirs(self._log_file.parent)
            f = open(self._log_file, "w")
            f.close()

    def _write_file(self):
        """Write to the file regardless of the LEVEL_NUMBER."""
        if self._disable_file:
            return

        with open(self._log_file, "a") as f:
            # The file log is to be written to the _log_file file
            f = open(self._log_file, "a")
            f.write(self._file_format)

    def _extract_args(self, message, other_str):
        """Extract the args and append them to the message,
        seperated by a space"""
        return "{} {}".format(message, ' '.join(other_str))

    def _write(self, message, args, LEVEL_NUMBER):
        """
            Write the logs.
            LEVEL_NUMBER is the levelnumber of the level that is calling the
            _write function.
        """
        self._make_format(self._extract_args(message, args))
        self._write_file()
        if LEVEL_NUMBER >= self.level:
            print(self._console_format)

    def _make_format(self, message):
        """
        Make the format of the string that is to be written.
        """
        console_format = Formatter.sub(self._console_format,
                                       self._passed_level, self.name)
        self._console_format = console_format + " {}".format(message)

        if self._disable_file:
            return

        # If file is not disabled, update the string.
        file_format = Formatter.sub(self._file_format,
                                    self._passed_level, self.name)
        self._file_format = file_format + " {}".format(message)

    def update_level(self, level):
        """
        Update all the instances of the class with the passed
        level.
        """
        # First check if the passed level is present in the supported ones
        if level not in self._level_number:
            print("Can't update logger level to invalid value")
            return

        for instance in Logger._instances:
            instance.level = self._level_number[level]

    def update_disable_file(self, disable_file):
        """
        Update the disable file variable.
        """
        for instance in Logger._instances:
            instance._disable_file = disable_file

    def update_format(self, format, file_format=None):
        """Update the format of all the instances.

        If the `file_format` is not passed, set the console_format
        as it.
        """
        # TODO: Verify format
        file_format = format if file_format is None else file_format

        for instance in Logger._instances:
            instance._console_format = format
            instance._file_format = file_format

    def list_available_levels(self):
        """
        List all the available logger levels.
        """
        for key in self._level_number:
            print("{} : {}".format(self._level_number[key], key.upper()))

    def hold(self):
        """
        Hold the screen by using input()
        """
        LEVEL_NUMBER = 0

        if LEVEL_NUMBER >= self.level:
            input("Screen hold! Press any key to continue")

    def debug(self, message, *args):
        """
        Add the message if the level is debug.
        """
        LEVEL_NUMBER = 0
        self._write(message, args, LEVEL_NUMBER)

    def info(self, message, *args):
        """
        Add the message if the level is info or less.
        """
        LEVEL_NUMBER = 1
        self._write(message, args, LEVEL_NUMBER)

    def warning(self, message, *args):
        """
        Add the message if the level is warning or less.
        """
        LEVEL_NUMBER = 2
        self._write(message, args, LEVEL_NUMBER)

    def error(self, message, *args):
        """
        Add the message if the level is error or less.
        """
        LEVEL_NUMBER = 3
        self._write(message, args, LEVEL_NUMBER)

    def critical(self, message, *args):
        """
        Add the message if the level is critical or less.
        """
        LEVEL_NUMBER = 4
        self._write(message, args, LEVEL_NUMBER)
        exit()
