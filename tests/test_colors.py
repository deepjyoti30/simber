"""Test the colors module of the logger."""

from simber.colors import ColorFormatter
from colorama import Fore


def test_color_formatter():
    """Test the color_formatter method of the class"""
    s = "%gnana%"
    output = Fore.GREEN + "nana" + Fore.RESET

    assert ColorFormatter().format_colors(s) == output, "Should be `Green`"


def test__replace_with_colors():
    """Test the _replace_with_colors method"""
    s = "%gnana%"
    output = Fore.GREEN + "nana" + Fore.RESET

    color_formatter = ColorFormatter()

    assert color_formatter._replace_with_colors(
        s, None) == output, "Should be `Green`"


def test__get_color_replacement():
    """Test the _get_color_replacement method"""
    s = "%rnana%"
    output = Fore.RED + "nana" + Fore.RESET

    color_formatter = ColorFormatter()
    output_returned = color_formatter._get_color_replacement(s, None)

    assert output_returned == output, "Should be {}, got {}".format(
        output, output_returned)
