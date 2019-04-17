import sys

sys.path.append(".")  # only works if run from the dir above

import arghandler


# arghandler.arg_option_dict
def test_should_return_blank_dict_if_given_no_valid_args():
    assert arghandler.arg_options_dict([]) == []


def test_should_return_two_valid_options_when_two_valid_args_are_given():
    args = ["--help", "--version"]
    expected_options = [
        {
            "option": "--help",
        },
        {
            "option": "--version",
        }
    ]
    assert arghandler.arg_options_dict(args) == expected_options


def test_should_return_one_valid_option_with_param_when_given_add_and_param():
    args = ["--add", "foo"]
    expected_options = [
        {
            "option": "--add",
            "param": "foo"
        }
    ]
    assert arghandler.arg_options_dict(args) == expected_options


def test_should_return_one_valid_option_with_param_when_given_only_one_valid_arg_and_param():
    args = ["--foo", "--add", "foo", "--bar"]
    expected_options = [
        {
            "option": "--add",
            "param": "foo"
        }
    ]
    assert arghandler.arg_options_dict(args) == expected_options


# arghandler.option_is_valid
def test_should_return_true_when_given_version():
    assert arghandler.option_is_valid("--version")


def test_should_return_false_when_given_foo():
    assert not arghandler.option_is_valid("--foo")


def test_should_return_false_when_given_malformed_but_close_to_version():
    assert not arghandler.option_is_valid("-version-")


def test_should_return_false_when_given_blank():
    assert not arghandler.option_is_valid("")


# arghandler.option_req_param
def test_should_return_true_when_given_add():
    assert arghandler.option_req_param("--add")


def test_should_return_false_when_given_version():
    assert not arghandler.option_req_param("--version")


# arghandler.handle_given_options
def test_should_return_true_when_given_help_as_the_only_option():
    options = [
        {
            "option": "--help"
        }
    ]
    assert arghandler.handle_given_options(options)


def test_should_return_true_when_given_no_options():
    options = []
    assert arghandler.handle_given_options(options)


def test_should_return_false_when_given_an_invalid_option():
    options = [
        {
            "option": "--foo"
        }
    ]
    assert not arghandler.handle_given_options(options)


def test_should_return_false_when_given_an_invalid_option_with_valid_options():
    options = [
        {
            "option": "--list"
        },
        {
            "option": "--foo"
        },
        {
            "option": "--add",
            "param": "bundaberg"
        }
    ]
    assert not arghandler.handle_given_options(options)


def test_should_return_true_when_given_no_options():
    options = {}
    assert arghandler.handle_given_options(options)
