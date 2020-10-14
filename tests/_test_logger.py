"""Test the Logger module"""

from simber.logger import Logger


def test__check_format():
    """Test the _check_format method"""
    logger = Logger("test")

    # Check the default
    assert logger._console_format == '%a[{levelname}]% [{logger}]', "Should be %a[{levelname}]% [{logger}]"
    assert logger._file_format == "[{levelname}] [{time}] [{filename}]", "Should be [{levelname}] [{time}] [{filename}]"

    # Check when just format is passed
    logger = Logger("test", format="nana")
    assert logger._console_format == "nana", "Should be `nana`"
    assert logger._file_format == "nana", "Should be `nana`"

    # Check when both format and file_format passed
    logger = Logger("test", format="format_nana", file_format="file_format_nana")
    assert logger._console_format == "format_nana", "Should be `format_nana`"
    assert logger._file_format == "file_format_nana", "Should be `file_format_nana`"


def test_update_format():
    """Test the update_format method"""
    logger1 = Logger("test1", format="nana")
    logger2 = Logger("test2", format="new_nana")

    logger2.update_format("second_nana")
    assert list(logger2._streams)[0].format == "second_nana", "Should be second_nana"


def test_update_disable_file():
    """Test the update_disable_file method"""
    logger1 = Logger("test1", disable_file=False)
    logger2 = Logger("test2", disable_file=True)

    logger2.update_disable_file(True)

    assert logger1._disable_file, "Should be true"
    assert logger2._disable_file, "Should be true"


def test_update_level():
    """Test the update_level method"""
    logger1 = Logger("test1", level="INFO")
    logger2 = Logger("test2", level="WARNING")

    logger2.update_level("DEBUG")

    assert list(logger1._streams)[0].level == logger1._level_number["DEBUG"], "Update level failed"
