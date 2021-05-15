"""Test if the formatter is working all right."""

from simber.formatter import Formatter
from typing import Dict
from datetime import datetime
from pytest import raises


def test__get_level():
    """Test the _get_level method of the formatter class"""
    level_details = Formatter()._get_level(1)
    expected_dict = {"levelno": 1,  "levelname": "INFO"}

    assert isinstance(level_details, Dict), "returntype should be dict"
    assert level_details == expected_dict, "Did not get expected level details"


def test__get_time():
    """
    Test if time is properly formatted
    """
    formatter = Formatter()
    with raises(TypeError):
        formatter._get_time(None)

    time_format = "%d/%m/%Y"
    assert formatter._get_time(
        time_format) == datetime.now().strftime(time_format),\
        "Should return the time in same format"
