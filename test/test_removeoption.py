import os
import sys

sys.path.append(".")

import pytest
import removeoption

#removeoption.image_is_added
def test_should_return_true_when_given_an_image_that_is_the_only_one_in_file():
	added_images = open(".added_images", "w")
	added_images.write("foo\n")
	added_images.close()
	assert removeoption.image_is_added("foo", ".added_images")
	os.remove(".added_images")

def test_should_return_true_when_given_an_image_that_exists_among_many():
	added_images = open(".added_images", "w")
	added_images.write("foo\n")
	added_images.write("bar\n")
	added_images.write("fizz\n")
	added_images.write("buzz\n")
	added_images.write("yes\n")
	added_images.close()
	assert removeoption.image_is_added("fizz", ".added_images")
	os.remove(".added_images")

def test_should_return_false_when_given_an_image_that_does_not_exist_among_many():
	added_images = open(".added_images", "w")
	added_images.write("foo\n")
	added_images.write("bar\n")
	added_images.write("fizz\n")
	added_images.write("buzz\n")
	added_images.write("yes\n")
	added_images.close()
	assert not removeoption.image_is_added("yas", ".added_images")
	os.remove(".added_images")

def test_should_return_false_when_given_an_empty_file():
	added_images = open(".added_images", "w")
	added_images.close()
	assert not removeoption.image_is_added("foo", ".added_images")
	os.remove(".added_images")

def test_should_return_false_when_given_a_non_existant_file():
	assert not removeoption.image_is_added("foo", ".added_images")

