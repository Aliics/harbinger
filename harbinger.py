import sys
import arghandler
import helpoption
import versionoption
import listoption
import addoption

VERSION = "1.0.0-SNAPSHOT"

OPTIONS = [
    {
        "option": "--help",
        "requires_param": False,
        "call": helpoption.call
    },
	{
        "option": "--version",
        "requires_param": False,
        "call": versionoption.call
    },
    {
        "option": "--list",
        "requires_param": False,
        "call": listoption.call
    },
    {
        "option": "--add",
        "requires_param": True,
        "call": addoption.call
    }
]

if __name__ == "__main__":
	options = arghandler.arg_options_dict(sys.argv)
	arghandler.handle_given_options(options)

