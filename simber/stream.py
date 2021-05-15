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
    disabled:       If the stream is disabled or not.
    """

    def __init__(
        self,
        stream: TextIOWrapper,
        level: str = None,
        format: str = None,
        disabled: bool = False,
        time_format: str = None
    ):
        self._passed_level = None
        self.stream = self._extract_stream(stream)
        self._level = self._extract_level(level)
        self._format = Default().file_format if format is None else format
        self._disabled = disabled
        self._time_format = time_format

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
        if not isinstance(passed_stream, TextIOWrapper):
            raise InvalidStream(type(passed_stream))

        return passed_stream

    def _make_format(self, message, level, frame, name):
        """
        Make the format of the string that is to be written.
        """
        _format = Formatter().sub(self._format,
                                  level, name, frame, message,
                                  time_format=self._time_format)

        return _format + '\n'

    @property
    def level(self) -> int:
        return self._level

    @level.setter
    def level(self, new_level: int):
        self._level = new_level

    @property
    def format(self) -> str:
        return self._format

    @format.setter
    def format(self, new_format: str):
        self._format = new_format

    @property
    def disabled(self) -> bool:
        return self._disabled

    @disabled.setter
    def disabled(self, new_value: bool):
        self._disabled = new_value

    @property
    def stream_name(self):
        return self.stream.name

    def __eq__(self, value):
        # If passed value is another object, we need to
        # compare the names
        if isinstance(value, OutputStream):
            return self.stream_name == value.stream_name

        # Else false
        return False

    def __hash__(self):
        return hash(self.stream_name)

    def __repr__(self):
        return self.stream_name

    def write(self, message, calling_level, frame, logger_name):
        """Write the message to the stream by making sure
        the calling level is above or equal to the level
        """
        if calling_level < self._level or self._disabled:
            return False

        _formatted_out = self._make_format(
            message, calling_level, frame, logger_name
        )

        params = {"end": ""}
        if self.stream.name not in Default().valid_stdout_names:
            # Add the stream since it won't be stdout
            params["file"] = self.stream

        print(_formatted_out, **params)
        return True
