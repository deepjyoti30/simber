"""Test if the formatter is working all right."""

from simber.formatter import Formatter
from typing import Dict


def test__get_level():
    """Test the _get_level method of the formatter class"""
    level_details = Formatter()._get_level(1)
    expected_dict = {"levelno": 1,  "levelname": "INFO"}

    assert isinstance(level_details, Dict), "returntype should be dict"
    assert level_details == expected_dict, "Did not get expected level details"
