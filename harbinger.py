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
		"desc": "Displays information about harbinger and it's commands.",
        "requires_param": False,
        "call": helpoption.call
    },
	{
        "option": "--version",
		"desc": "Outputs the current version of harbinger.",
        "requires_param": False,
        "call": versionoption.call
    },
    {
        "option": "--list",
		"desc": "Outputs a list of docker containers and images that are either currently up, or can be brought up.",
        "requires_param": False,
        "call": listoption.call
    },
    {
        "option": "--add",
		"desc": "Add an image to your cluster. Making it available to be run in as a container.",
        "requires_param": True,
        "call": addoption.call
    }
]

if __name__ == "__main__":
	options = arghandler.arg_options_dict(sys.argv)
	arghandler.handle_given_options(options)

