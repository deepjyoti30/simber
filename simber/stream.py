"""Handle output streams of the logger."""

from _io import TextIOWrapper

from simber.configurations import Default
from simber.exceptions import InvalidLevel


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
            raise

        return passed_stream
