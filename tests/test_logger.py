"""Test the Logger module"""

from os import remove

from simber.logger import Logger
from simber.configurations import Default


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
    logger = Logger("test", format="format_nana",
                    file_format="file_format_nana")
    assert logger._console_format == "format_nana", "Should be `format_nana`"
    assert logger._file_format == "file_format_nana", "Should be `file_format_nana`"


def test_update_format():
    """Test the update_format method"""
    logger1 = Logger("test1", format="nana")
    logger2 = Logger("test2", format="new_nana")

    logger2.update_format("second_nana")
    assert list(logger2._streams)[
        0].format == "second_nana", "Should be second_nana"


def test_update_disable_file():
    """Test the update_disable_file method"""
    logger1 = Logger("test1", disable_file=False)
    logger2 = Logger("test2", disable_file=True)

    logger2.update_disable_file(True)

    assert logger1._disable_file, "Should be true"
    assert logger2._disable_file, "Should be true"


def test_stdout_update_level():
    """Test the update_level method"""
    logger1 = Logger("test1", level="INFO")
    logger2 = Logger("test2", level="WARNING")

    logger2.update_level("DEBUG")

    # Check if all the stdout streams have the same level
    streams = [
        s.level for s in logger1.streams if s.stream_name
        in Default().valid_stdout_names]

    assert streams == ([0] * len(streams)), "Update level failed"


def test_remove_stream():
    """
    Test the remove stream method of the logger.
    """
    file_path = "test.txt"
    logger1 = Logger("test1", log_path=file_path)

    # The first stream should be a file stream
    file_stream = logger1.streams[0]
    logger1.remove_stream(file_stream)

    # Remove the test.txt file
    remove(file_path)

    assert len(logger1.streams) == 1, "Removing stream failed"
