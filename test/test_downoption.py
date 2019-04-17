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
