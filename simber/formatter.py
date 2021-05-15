"""Formatter to handle everything related to
the format of the strings that are printed.
"""

from datetime import datetime

from simber.configurations import Default
from simber.colors import ColorFormatter


class Formatter(object):
    """Format the passed strings according to the
    passed arguements.

    The string would be able to contain certain
    special format options in order to give flexibilty
    to the users.
    """

    def __init__(self):
        pass

    def _get_time(self, strformat: str = "%d/%m/%Y %H:%M:%S"):
        """Get the time, based on the string passed."""
        if type(strformat) != str:
            raise TypeError(
                f"strformat should be str, {type(strformat)} passed")
        return datetime.now().strftime(strformat)

    def _get_caller_details(self, last_to_last_frame):
        """Get the name of the file that called the logger."""
        return {
            'name': last_to_last_frame.f_code.co_name,
            'filename': last_to_last_frame.f_code.co_filename,
            'line_no': last_to_last_frame.f_lineno
        }

    def _get_level(self, level_no: int):
        """Get the level info from the passed level"""
        level_info = Default().level_number

        if level_no not in list(level_info.values()):
            raise Exception("{}: Not a valid level".format(level_no))

        return {
            'levelno': level_no,
            'levelname': [key for (key, value) in level_info.items()
                          if value == level_no][0]
        }

    def _add_message_if_not_present(self, unformatted_str):
        """Add the message keyword to the string if it is not already
        present.

        The message string will always be appended to the string."""
        if '{message}' not in unformatted_str:
            unformatted_str += " {message}"

        return unformatted_str

    def sub(self, unformatted_str, level, name, frame, message, time_format):
        """Format the passed strings with the paramaters
        as possible.

        :param unformatted_str: Unformatted String to be substitued
        with.
        :param level: The level logger is currently calling from.
        :param name: The name of the logger
        :return: The formatted string
        :rtype: str
        """
        current_time = self._get_time(
            **({"strformat": time_format} if time_format is not None else {}))
        caller_info = self._get_caller_details(frame)
        level_info = self._get_level(level)

        # Add message if not already present
        unformatted_str = self._add_message_if_not_present(
            unformatted_str)

        unformatted_str = unformatted_str.format(
            time=current_time,
            filename=caller_info['filename'],
            funcname=caller_info['name'],
            lineno=caller_info['line_no'],
            levelname=level_info['levelname'],
            levelno=level_info['levelno'],
            logger=name,
            message=message
        )

        # Pass it through the color formatter
        unformatted_str = ColorFormatter().format_colors(unformatted_str,
                                                         level_info["levelname"])
        return unformatted_str
