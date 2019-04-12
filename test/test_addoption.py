import os
import sys

sys.path.append(".")

import pytest
import addoption
import listoption

#addoption.image_exists
def test_should_return_true_when_given_the_only_valid_docker_image():
	docker_output = ["image version id mod time time size"]
	images = listoption.format_docker_images_list(docker_output)
	assert addoption.image_exists("image", images)

def test_should_return_true_even_given_a_big_list_valid_docker_images():
	docker_output = [
		"image0 version id mod time time size",
		"image1 version id mod time time size",
		"image2 version id mod time time size",
		"image3 version id mod time time size",
		"image4 version id mod time time size",
		"image5 version id mod time time size",
		"image6 version id mod time time size",
		"image7 version id mod time time size",
		"image8 version id mod time time size",
		"image9 version id mod time time size",
		"image10 version id mod time time size",
		"image11 version id mod time time size",
		"image12 version id mod time time size",
		"image13 version id mod time time size",
		"image14 version id mod time time size",
		"image15 version id mod time time size",
		"image16 version id mod time time size",
		"image17 version id mod time time size",
		"image18 version id mod time time size",
		"image19 version id mod time time size"
	]
	images = listoption.format_docker_images_list(docker_output)
	assert addoption.image_exists("image7", images)

def test_should_false_when_no_image_is_found_even_from_a_big_list():
	docker_output = [
		"image0 version id mod time time size",
		"image1 version id mod time time size",
		"image2 version id mod time time size",
		"image3 version id mod time time size",
		"image4 version id mod time time size",
		"image5 version id mod time time size",
		"image6 version id mod time time size",
		"image7 version id mod time time size",
		"image8 version id mod time time size",
		"image9 version id mod time time size",
		"image10 version id mod time time size",
		"image11 version id mod time time size",
		"image12 version id mod time time size",
		"image13 version id mod time time size",
		"image14 version id mod time time size",
		"image15 version id mod time time size",
		"image16 version id mod time time size",
		"image17 version id mod time time size",
		"image18 version id mod time time size",
		"image19 version id mod time time size"
	]
	images = listoption.format_docker_images_list(docker_output)
	assert not addoption.image_exists("image20", images)

def test_should_return_false_when_search_is_over_an_empty_list():
	docker_output = []
	images = listoption.format_docker_images_list(docker_output)
	assert not addoption.image_exists("image", images)

#addoption.file_contains_image
def test_should_return_true_when_image_is_already_in_file():
	addoption.append_image_to_file("foo_image", "added_images")
	assert addoption.file_contains_image("foo_image", "added_images")
	os.remove("added_images")

def test_should_return_false_when_image_is_not_in_file():
	addoption.append_image_to_file("foo_image", "added_images")
	assert not addoption.file_contains_image("bar_image", "added_images")
	os.remove("added_images")

def test_should_return_false_when_image_is_non_existant():
	assert not addoption.file_contains_image("foo", ".add_images")

#addoption.append_image_to_file
def test_should_create_a_new_file_and_append_the_image_name():
	addoption.append_image_to_file("foo_image", "added_images")
	added_images = open("added_images")
	images = added_images.readlines()
	added_images.close()
	os.remove("added_images")
	assert images[0] == "{}\n".format("foo_image")

def test_only_append_image_name_if_image_is_not_already_stored():
	addoption.append_image_to_file("foo_image", "added_images")
	addoption.append_image_to_file("foo_image", "added_images")
	added_images = open("added_images")
	images = added_images.readlines()
	added_images.close()
	os.remove("added_images")
	assert len(images) == 1

