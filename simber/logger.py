"""A simple, minimal and powerful logger for Python.

It was merely built because of some restrictions that the
Python's default logging library has. This library is
aimed as a simple, minimal yet powerful logging library
for all Python apps.

Copyright (c) 2020 Deepjyoti Barman <deep.barman30@gmail.com>
"""
from pathlib import Path
import os
from sys import _getframe, stdout

from simber.configurations import Default
from simber.stream import OutputStream
from simber.exceptions import InvalidLevel, InvalidOutputStream


class Logger(object):
    """Handle the logging through one class. This will be the
    class exposed to the users.

    This class will have various methods but the most important
    methods are the ones that will allow the user to log at
    various levels.

    Logger will accept various paramaters but in order to keep
    the __init__ method simple, this params are accepted through a
    kwargs paramater. All the paramaters are optional.

    Available options:

    format:             Format of the console output string.
    file_format:        Format of the file output string. If `format`
                        is passed and this is not passed, then `format`
                        is copied to this.
    log_path:           Path to the log file or directory. If it is a dir
                        then the log file is created in the directory. If
                        it is a file, logger will start appending to the file.
                        If not passed, writing to file will be disabled.
    level:              Minimum level that the logger should verbose in. It is
                        a string that is by default set to `INFO`. All accepted
                        values are `DEBUG, INFO, WARNING, ERROR, CRITICAL`.
                        This list can also be accessed by the
                        `list_available_levels` method.
    file_level:         Minimum level that the logger should verbose file
                        outputs in. By default this is set to the minimum
                        level possible.
    disable_file:       If to disable writing to the file. This is
                        set to False if the log_path is passed. If log_path is
                        invalid or None, this is set to True.
    update_all:         If to update all the instances initialized before init
                        self logger. If passed True, all the logger instances
                        previsouly init will be updated with the `format`,
                        `disable_file` and `level` attribute.
    """

    _instances = []
    _streams = set()

    def __init__(
        self,
        name,
        **kwargs
    ):
        self.name = name
        self._level_number = Default().level_number
        self._passed_level = kwargs.get("level", "INFO")
        self._passed_file_level = kwargs.get("file_level", "DEBUG")
        self.level = self._level_number[self._passed_level]
        self._file_level = self._level_number[self._passed_file_level]
        self._disable_file = kwargs.get("disable_file", False)
        self._log_file = self._check_logfile(kwargs.get("log_path", None))

        self._check_format(kwargs.get("format", None),
                           kwargs.get("file_format", None))
        self._init_default_streams()

        # Update all instances, if asked to
        if kwargs.get("update_all", False):
            self.update_format(self._console_format, self._file_format)
            self.update_disable_file(self._disable_file)
            self.update_level(self._passed_level)

        self._instances.append(self)

    def _init_default_streams(self):
        """Initialize the default streams

        Logger class will by default, initialize two streams.
        Those are:

        stdout - Required
        file_stream - If disabled, this will be skipped
        """
        # Initialize the default stdout stream
        self._streams.add(
            OutputStream(stdout, self._passed_level, self._console_format)
        )

        # If log_file is invalid, skip creating the file
        # stream.
        if self._log_file is None:
            return

        # Initialize the file stream
        # Even if the disable_file flag is passed, add this stream
        # because file can be enabled later.
        self._streams.add(
            OutputStream(
                open(self._log_file, "a"),
                self._passed_file_level,
                self._file_format,
                self._disable_file
            ))

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

    def _check_logfile(self, log_path):
        """
        Check if the passed logfile path is present.
        If not present then create it.
        """
        # If the log_file path is not passed, disable the
        # logging to file
        if log_path is None:
            self._disable_file = True
            return log_path

        # If it is passed, make it a Path object
        log_path = Path(log_path).expanduser()

        # Check if the file is a dir
        # If it is, then append the file name to the log
        # path and continue
        if log_path.is_dir():
            log_path = log_path.joinpath(Default().log_file_name)

        if not log_path.exists():
            # Below check is important if the passed log path
            # is a file name inside some directory
            if not log_path.parent.exists():
                os.makedirs(log_path.parent)
            f = open(log_path, "w")
            f.close()

        return str(log_path)

    def _extract_args(self, message, other_str):
        """Extract the args and append them to the message,
        seperated by a space"""
        return "{} {}".format(message, ' '.join(other_str))

    def _write(self, message, args, level):
        """
            Write the logs.
            level is the levelnumber of the level that is calling the
            _write function.
        """
        # Get the frame of the caller
        caller_frame = _getframe().f_back.f_back
        message = self._extract_args(message, args)

        for stream in self._streams:
            stream.write(
                message,
                level,
                caller_frame,
                self.name
            )

    def _disable_file_streams(self):
        """Disable the file streams.

        We will check if the streams are files or standard,
        based on that, we can disable the streams accordingly.

        This won't have any effect if the log_file path was not
        passed during init.
        """
        valid_names = Default().valid_stdout_names

        for stream in self._streams:
            if stream.stream_name not in valid_names:
                stream.disabled = self._disable_file

    def update_level(self, level):
        """
        Update all the streams with the passed level.
        """
        # First check if the passed level is present in the supported ones
        if level not in self._level_number:
            raise InvalidLevel(level)

        for stream in self._streams:
            stream.level = self._level_number[level]

    def update_disable_file(self, disable_file):
        """
        Update the disable file variable.
        """
        self._disable_file = disable_file
        self._disable_file_streams()

    def update_format(self, format, file_format=None):
        """Update the format of all the instances.

        We need to update the instances seperately based
        on the type of the stream.
        """
        valid_stdout_names = Default().valid_stdout_names
        file_format = format if file_format is None else file_format

        for stream in self._streams:
            if stream.stream_name in valid_stdout_names:
                # Probably a console format
                stream.format = format
            else:
                # Probably a file stream
                stream.format = file_format

    def update_format_console(self, format):
        """Update the format for all the non file instances

        This is useful if an app requires different formats
        for file and console and both are updated throug
        one instance.
        """
        valid_names = Default().valid_stdout_names

        for stream in self._streams:
            if stream.stream_name not in valid_names:
                stream.format = format

    def add_stream(self, stream_to_be_added: OutputStream):
        """Add the passed stream to the _streams class so
        that it can be used to write to that as well.
        """
        if not isinstance(stream_to_be_added, OutputStream):
            raise InvalidOutputStream(type(stream_to_be_added))

        self._streams.add(stream_to_be_added)

    def get_log_file(self):
        """Get the log file that is being written to.

        This is just to support backward functionality for ytmdl
        """
        return self._log_file

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
