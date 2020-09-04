"""Test the Logger module"""

from simber.logger import Logger


def test__check_format():
    """Test the _check_format method"""
    logger = Logger("test")

    # Check the default
    assert logger._console_format == "", "Should be ``"
    assert logger._file_format == "", "Should be ``"

    # Check when just format is passed
    logger = Logger("test", format="nana")
    assert logger._console_format == "nana", "Should be `nana`"
    assert logger._file_format == "nana", "Should be `nana`"

    # Check when both format and file_format passed
    logger = Logger("test", format="format_nana", file_format="file_format_nana")
    assert logger._console_format == "format_nana", "Should be `format_nana`"
    assert logger._file_format == "file_format_nana", "Should be `file_format_nana`"

    # Check when only file_format is passed
    logger = Logger("test", file_format="nana")
    assert logger._console_format == "", "Should be ``"
    assert logger._file_format == "nana", "Should be `nana`"
