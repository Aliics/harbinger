import sys

sys.path.append(".")

import pytest
import listoption

# listoption.docker_image_list
def test_should_return_two_dicts_of_docker_image_info_when_given_two_valid_strings():
	docker_output = ["foo bar wasd qwerty weeks ago yes", "cake tastes really good weeks ago man"]
	expected = [
		{
			"image": "foo",
			"version": "bar",
			"id": "wasd",
			"mod_time": "qwerty weeks ago",
			"size": "yes"
		},
		{
			"image": "cake",
			"version": "tastes",
			"id": "really",
			"mod_time": "good weeks ago",
			"size": "man"
		}
	]
	assert listoption.format_docker_images_list(docker_output) == expected

def test_should_return_one_dict_of_docker_image_info_when_given_one_invalid_string():
	docker_output = ["foo bar wasd qwerty", "cake tastes really good years ago man"]
	expected = [
		{
			"image": "cake",
			"version": "tastes",
			"id": "really",
			"mod_time": "good years ago",
			"size": "man"
		}
	]
	assert listoption.format_docker_images_list(docker_output) == expected

# listoption.shorten_image_name
def test_should_return_foo_when_given_ecr_url_with_image_name_foo():
	ecr_url = "825119612905.dkr.ecr.eu-west-1.amazonaws.com/foo"
	assert listoption.shorten_image_name(ecr_url) == "foo"

def test_should_return_blank_when_given_an_empty_string():
	blank_string = ""
	assert listoption.shorten_image_name(blank_string) == ""

def test_should_return_what_was_given_when_given_a_plain_string():
	plain_string = "funname"
	assert listoption.shorten_image_name(plain_string) == "funname"
