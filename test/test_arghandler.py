import sys
import pytest

sys.path.append(".") # only works if run from the dir above

import arghandler

def test_should_return_blank_dict_if_given_no_valid_args():
	assert arghandler.arg_options_dict([]) == []

def test_should_return_two_valid_options_when_two_valid_args_are_given():
	args = ["--help", "--version"]
	expected_options = [
		{
			"option": "--help",
			"param": None
		}
	]
	assert arghandler.arg_options_dict(args) == expected_options

