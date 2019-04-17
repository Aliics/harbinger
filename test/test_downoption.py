import sys

sys.path.append(".")

import downoption


def test_should_return_expected_container_id_when_given_image_name_that_matches_only_container():
    current_containers = [
        "f395d8187d40 foo \"/bin/sh -c ./run.sh\" 31 minutes ago Up 31 minutes 25735/tcp sharp_kalam"
    ]
    containers = downoption.list_container_ids(["foo"], current_containers)
    expected = ["f395d8187d40"]
    assert containers == expected


def test_should_return_multi_container_ids_when_image_has_multiple_instances_up():
    current_containers = [
        "f395d8187d40 foo \"/bin/sh -c ./run.sh\" 31 minutes ago Up 31 minutes 25735/tcp sharp_kalam",
        "f395d8187d41 foo \"/bin/sh -c ./run.sh\" 32 minutes ago Up 32 minutes 25735/tcp sharp_kalam"
    ]
    containers = downoption.list_container_ids(["foo"], current_containers)
    expected = ["f395d8187d40", "f395d8187d41"]
    assert containers == expected


def test_should_return_multi_container_ids_when_multiple_images_have_multiple_instances_up():
    current_containers = [
        "f395d8187d40 foo \"/bin/sh -c ./run.sh\" 31 minutes ago Up 31 minutes 25735/tcp sharp_kalam",
        "f395d8187d41 foo \"/bin/sh -c ./run.sh\" 32 minutes ago Up 32 minutes 25735/tcp sharp_kalam",
        "f395d8187d42 foobar \"/bin/sh -c ./run.sh\" 32 minutes ago Up 32 minutes 25735/tcp sharp_kalam",
        "f395d8187d43 foobar \"/bin/sh -c ./run.sh\" 32 minutes ago Up 32 minutes 25735/tcp sharp_kalam"
    ]
    containers = downoption.list_container_ids(["foo", "foobar"], current_containers)
    expected = ["f395d8187d40", "f395d8187d41", "f395d8187d42", "f395d8187d43"]
    assert containers == expected


def test_should_return_blank_when_desired_image_is_not_in_cluster():
    current_containers = [
        "f395d8187d40 foo \"/bin/sh -c ./run.sh\" 31 minutes ago Up 31 minutes 25735/tcp sharp_kalam",
        "f395d8187d41 foo \"/bin/sh -c ./run.sh\" 32 minutes ago Up 32 minutes 25735/tcp sharp_kalam",
        "f395d8187d42 foobar \"/bin/sh -c ./run.sh\" 32 minutes ago Up 32 minutes 25735/tcp sharp_kalam",
        "f395d8187d43 foobar \"/bin/sh -c ./run.sh\" 32 minutes ago Up 32 minutes 25735/tcp sharp_kalam"
    ]
    containers = downoption.list_container_ids(["fizz"], current_containers)
    expected = []
    assert containers == expected


def test_should_return_only_one_set_of_container_ids_even_when_multiple_exist():
    current_containers = [
        "f395d8187d40 foo \"/bin/sh -c ./run.sh\" 31 minutes ago Up 31 minutes 25735/tcp sharp_kalam",
        "f395d8187d41 foo \"/bin/sh -c ./run.sh\" 32 minutes ago Up 32 minutes 25735/tcp sharp_kalam",
        "f395d8187d42 foobar \"/bin/sh -c ./run.sh\" 32 minutes ago Up 32 minutes 25735/tcp sharp_kalam",
        "f395d8187d43 foobar \"/bin/sh -c ./run.sh\" 32 minutes ago Up 32 minutes 25735/tcp sharp_kalam"
    ]
    containers = downoption.list_container_ids(["foobar"], current_containers)
    expected = ["f395d8187d42", "f395d8187d43"]
    assert containers == expected


def test_should_return_blank_when_no_containers_are_up():
    current_containers = []
    containers = downoption.list_container_ids(["foo"], current_containers)
    expected = []
    assert containers == expected
