import os
import sys

sys.path.append(".")

import upoption


def test_should_give_list_of_two_strings_when_file_given_has_two_objects():
    added_images = open(".added_images", "w")
    added_images.write("image1\n")
    added_images.write("image2\n")
    added_images.close()
    expected = ["image1", "image2"]
    images = upoption.list_added_images(".added_images")
    assert len(images) == 2
    assert images == expected
    os.remove(".added_images")


def test_should_return_a_blank_list_when_file_contains_nothing():
    added_images = open(".added_images", "w")
    added_images.close()
    images = upoption.list_added_images(".added_images")
    assert images == []
    os.remove(".added_images")


def test_should_return_a_blank_list_when_file_does_not_exist():
    images = upoption.list_added_images(".added_images")
    assert images == []
