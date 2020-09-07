"""Define exceptions for the logger class"""

from simber.configurations import Default


class InvalidLevel(Exception):
    """Exception for invalid level.

    This will be raise if the level the user
    passed is not valid.
    """
    def __init__(self, message, level):
        super().__init__()

        self.message = self._build_message(level)

    def _build_message(self, level):
        """Build a message to show the user"""
        message = "{level}: is an invalid level."\
                  "Try one of these: {all_levels}"
        return message.format(
            level=level,
            all_levels=dict(Default().level_number.keys())
        )

    def __str__(self):
        return self.message
