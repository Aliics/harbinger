import sys
import shutil

sys.path.append(".")

import helpoption


# helpoption.format_help_text
def test_should_return_the_exact_expected_string():
    terminal_width = shutil.get_terminal_size().columns
    expected = "option     | desc\n"
    expected += helpoption.draw_line(terminal_width)
    expected += "--help     | Displays information about harbinger and it's commands.\n"
    expected += "--version  | Outputs the current version of harbinger.\n"
    expected += "--list     | Outputs a list of docker containers and images that are either currently up, or can be brought up.\n"
    expected += "--add      | Add an image to your cluster. Making it available to be run in as a container.\n"
    expected += "--remove   | Remove an image from your cluster, so it won't be brought up as a container.\n"
    expected += "--up       | Brings your docker cluster up.\n"
    expected += "--down     | Brings down your entire docker cluster.\n"

    assert helpoption.format_help_text() == expected


# helpoption.draw_line
def test_should_return_five_equal_characters():
    assert helpoption.draw_line(5) == "====="


def test_should_return_two_plus_characters():
    assert helpoption.draw_line(2, "+") == "++"
