import sys

sys.path.append(".")

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


# listoption.beautify_docker_image_dict
def test_should_return_expected_when_given_a_valid_list_of_dicts():
    list_of_dict = [
        {
            "image": "cake",
            "version": "tastes",
            "id": "really",
            "mod_time": "good years ago",
            "size": "man"
        }
    ]
    expected = "image           | version                   | id              | mod_time        | size           \n"
    expected += "=================================================================================================\n"
    expected += "cake            | tastes                    | really          | good years ago  | man            \n"
    assert listoption.beautify_docker_image_dict(list_of_dict) == expected


def test_should_return_a_blank_string_when_given_an_empty_list():
    assert listoption.beautify_docker_image_dict([]) == ""


def test_should_return_max_bounds_characters_when_given_a_list_dict_with_really_long_names():
    list_of_dict = [
        {
            "image": "cakeisareallylongname",
            "version": "tastesisareallylongname",
            "id": "reallyisareallylongname",
            "mod_time": "good years agoisareallylongname",
            "size": "manisareallylongname"
        }
    ]
    expected = "image           | version                   | id              | mod_time        | size           \n"
    expected += "=================================================================================================\n"
    expected += "cakeisareallylo | tastesisareallylongname   | reallyisareally | good years agoi | manisareallylon\n"
    assert listoption.beautify_docker_image_dict(list_of_dict) == expected
