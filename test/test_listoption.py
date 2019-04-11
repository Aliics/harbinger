import sys

sys.path.append(".")

import pytest
import listoption

# listoption.docker_image_list
def test_should_return_two_dicts_of_docker_image_info_when_given_two_valid_strings():
	docker_output = ["foo bar wasd qwerty yes", "cake tastes really good man"]
	expected = [
		{
			"image": "foo",
			"version": "bar",
			"id": "wasd",
			"mod_time": "qwerty",
			"size": "yes"
		},
		{
			"image": "cake",
			"version": "tastes",
			"id": "really",
			"mod_time": "good",
			"size": "man"
		}
	]
	assert listoption.format_docker_images_list(docker_output) == expected

def test_should_return_one_dict_of_docker_image_info_when_given_one_invalid_string():
	docker_output = ["foo bar wasd qwerty", "cake tastes really good man"]
	expected = [
		{
			"image": "cake",
			"version": "tastes",
			"id": "really",
			"mod_time": "good",
			"size": "man"
		}
	]
	assert listoption.format_docker_images_list(docker_output) == expected

