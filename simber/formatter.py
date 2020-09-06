"""Formatter to handle everything related to
the format of the strings that are printed.
"""

from datetime import datetime
from sys import _getframe

from simber.configurations import Default


class Formatter(object):
    """Format the passed strings according to the
    passed arguements.

    The string would be able to contain certain
    special format options in order to give flexibilty
    to the users.
    """
    def __init__(self):
        pass

    def _get_time(self, strformat="%d/%m/%Y %H:%M:%S"):
        """Get the time, based on the string passed."""
        return datetime.now().strftime(strformat)

    def _get_caller_details(self):
        """Get the name of the file that called the logger."""
        last_to_last_frame = _getframe().f_back.f_back
        return {
            'name': last_to_last_frame.f_code.co_name,
            'filename': last_to_last_frame.f_code.co_filename,
            'line_no': last_to_last_frame.f_back.f_lineno
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

    @staticmethod
    def sub(unformatted_str, level, name):
        """Format the passed strings with the paramaters
        as possible.

        :param unformatted_str: Unformatted String to be substitued
        with.
        :param level: The level logger is currently calling from.
        :param name: The name of the logger
        :return: The formatted string
        :rtype: str
        """
        formatter = Formatter()
        current_time = formatter._get_time()
        caller_info = formatter._get_caller_details()
        level_info = formatter._get_level(level)

        return unformatted_str.format(
            time=current_time,
            filename=caller_info['filename'],
            funcname=caller_info['name'],
            lineno=caller_info['line_no'],
            levelname=level_info['levelname'],
            levelno=level_info['levelno'],
            logger=name
        )
