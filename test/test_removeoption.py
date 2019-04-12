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

# removeoption.remove_added_image
def test_should_remove_image_from_file_when_given_valid_image():
	added_images = open(".added_images", "w")
	added_images.write("foobar\n")
	added_images.close()
	removeoption.remove_added_image("foobar", ".added_images")
	added_images = open(".added_images", "r")
	currently_added = added_images.readlines()
	added_images.close()
	assert len(currently_added) == 0
	os.remove(".added_images")

def test_should_not_remove_anything_when_given_an_image_that_is_not_in_file():
	added_images = open(".added_images", "w")
	added_images.write("foo\n")
	added_images.close()
	removeoption.remove_added_image("bar", ".added_images")
	added_images = open(".added_images", "r")
	currently_added = added_images.readlines()
	added_images.close()
	assert len(currently_added) == 1
	os.remove(".added_images")

def test_should_only_remove_one_image_from_file_in_a_file_of_many():
	added_images = open(".added_images", "w")
	added_images.write("foo\n")
	added_images.write("bar\n")
	added_images.write("fizz\n")
	added_images.write("buzz\n")
	added_images.write("charles\n")						
	added_images.close()
	removeoption.remove_added_image("bar", ".added_images")
	added_images = open(".added_images", "r")
	currently_added = added_images.readlines()
	added_images.close()
	assert len(currently_added) == 4
	os.remove(".added_images")

