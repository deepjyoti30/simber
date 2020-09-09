"""Define exceptions for the logger class"""

from simber.configurations import Default


class InvalidLevel(Exception):
    """Exception for invalid level.

    This will be raise if the level the user
    passed is not valid.
    """
    def __init__(self, level):
        super().__init__()

        self.message = self._build_message(level)

    def _build_message(self, level):
        """Build a message to show the user"""
        message = "{level}: is an invalid level."\
                  " Expected one of these: {all_levels}"
        return message.format(
            level=level,
            all_levels=list(Default().level_number.keys())
        )

    def __str__(self):
        return self.message


class InvalidStream(Exception):
    """Exception for invalid stream

    If the passed stream is not valid, i:e not
    of type TextIOWrapper, than raise this exception.
    """
    def __init__(self, passed_type):
        super().__init__()

        self.message = self._build_message(passed_type)

    def _build_message(self, passed_type):
        """Build a message to show the user when this exception
        arises."""
        message = "Expected <class 'TextIOWrapper'>, got {}".format(
            passed_type)

        return message

    def __str__(self):
        return self.message


class InvalidOutputStream(Exception):
    """Exception for invalid output stream

    If the passed stream is not of valid OutputStream type,
    then raise this exception.
    """
    def __init__(self, passed_type):
        super().__init__()

        self.message = self._build_message(passed_type)

    def _build_message(self, passed_type):
        return "Expected <class 'OutputStream'>, got {}".format(passed_type)

    def __str__(self):
        return self.message
