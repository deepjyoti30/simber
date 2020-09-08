"""Handle output streams of the logger."""

from _io import TextIOWrapper

from simber.configurations import Default
from simber.exceptions import InvalidLevel, InvalidStream
from simber.formatter import Formatter


class OutputStream(object):
    """Handle the output streams of the logger.

    Each stream needs to have three properties.

    level:          The minimum level the stream will output in.
    format:         The format in which the stream will output in.
    stream:         The stream itself. It can be an TextIOWrapper
                    object that will have a write method which will
                    be used to write to it.
    """
    def __init__(
        self,
        stream: TextIOWrapper,
        level: str = None,
        format: str = None
    ):
        self._passed_level = None
        self.stream = self._extract_stream(stream)
        self._level = self._extract_level(level)
        self._format = Default().file_format if format is None else format

    def _extract_level(self, passed_level: str):
        """Extract the passed level.

        If the passed_level is None, then set it to the
        default level. Else, make sure that the passed level
        is valid and accordingly return the level in int.
        """
        level_map = Default().level_number

        # If level is not passed
        if passed_level is None:
            return level_map["INFO"]

        # If it is passed, make sure it's valid
        if passed_level not in list(level_map.keys()):
            raise InvalidLevel(passed_level)

        self._passed_level = passed_level
        return level_map[passed_level]

    def _extract_stream(self, passed_stream: TextIOWrapper):
        """Extract the passed stream.

        If the passed stream is not a valid one, raise an exception,
        else, just return it.
        """
        if type(passed_stream) != TextIOWrapper:
            raise InvalidStream(type(passed_stream))

        return passed_stream

    def _make_format(self, message, level, frame, name):
        """
        Make the format of the string that is to be written.
        """
        _format = Formatter.sub(self._format,
                                level, name, frame)
        _format += " {}".format(message)

        return _format + '\n'

    def update_level(self, new_level):
        """Allow updating the level from other modules"""
        self._level = new_level

    def update_format(self, new_format):
        """Allow updating the format from other modules"""
        self._format = new_format

    def write(self, message, calling_level, frame, logger_name):
        """Write the message to the stream by making sure
        the calling level is above or equal to the level
        """
        if calling_level < self._level:
            return False

        self.stream.write(self._make_format(
            message, calling_level, frame, logger_name
        ))
        return True
