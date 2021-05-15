"""Handle formatting related to colors."""

from colorama import Fore

from re import findall
from typing import Dict

from simber.configurations import Default
from simber.exceptions import InvalidLevel


class ColorFormatter(object):
    """Format colors to the passed string.

    The colors will be decided based on the level
    passed and accordingly replaced in the string
    and returned.

    Following is the color mapping based on the levels

    DEBUG:          Blue
    INFO:           Green
    WARNING:        Yellow
    ERROR:          Red
    CRITICAL:       Red
    """

    def __init__(self):
        self._color_mapping = {
            'g': Fore.GREEN,
            'r': Fore.RED,
            'y': Fore.YELLOW,
            'b': Fore.BLUE,
            'm': Fore.MAGENTA,
            'c': Fore.CYAN,
            'w': Fore.WHITE,
            'n': Fore.BLACK
        }
        self._default = Fore.RESET

    @property
    def color_mapping(self) -> Dict:
        return self._color_mapping

    @property
    def default(self) -> str:
        return self._default

    def _determine_color_from_level(self, level):
        """Determine the color to be used based on the level
        of the logger"""
        if level is None or level not in Default().level_number:
            raise InvalidLevel(level)

        return Default().color_level_map.get(level, None)

    def _get_color_replacement(self, special_str, level):
        """Get the colored replacement of the passed
        special str.

        The string will be of the following type
        `%gsample_string%`

        where, g is the color code. We need to replace
        `%g` with the color code and we need to replace the
        ending `%` with proper reset code.
        """
        prefix = special_str[:2]
        postfix = special_str[-1]  # This will always be % tho
        color = prefix[1]

        if color == "a":
            # TODO: Check if level is None
            color = self._determine_color_from_level(level)

        replaced_color = self._color_mapping.get(color, self._default)

        # Do the substitution now
        special_str = special_str.replace(prefix, replaced_color)
        special_str = special_str.replace(postfix, self._default)

        return special_str

    def _replace_with_colors(self, str_passed, level):
        """Find the special characters in the string
        and replace them with the colors as passed by the
        user.
        """
        occurences = findall(r'%.*?%', str_passed)

        for occurence in occurences:
            str_passed = str_passed.replace(occurence,
                                            self._get_color_replacement(
                                                occurence, level))

        return str_passed

    def format_colors(self, str_passed, level: str = None):
        """Format the str_passed with the colors as asked by
        the user and return a formatted string accordingly.
        """
        return self._replace_with_colors(str_passed, level)
