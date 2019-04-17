import os
import upoption
from multiprocessing import Process


def list_container_ids(added_images, current_containers):
    container_ids = []
    for current_container in current_containers:
        id = current_container.split()
        container_ids.append(id[0])
    return container_ids


def stop_docker_container(image_name):
    os.popen("docker stop {}".format(image_name)).close()


def call(param):
    try:
        added_images = upoption.list_added_images(".added_images")
        current_containers = list_container_ids(added_images)
        if len(current_containers) == 0:
            print("Nice try! There are no containers even in the cluster. ;^)")
            return True
        processes = []
        for current_container in current_containers:
            docker_runner = Process(target=stop_docker_container, args=(current_container,))
            docker_runner.start()
            processes.append(docker_runner)
        for process in processes:
            process.join()
        return True
    except:
        print("Uh oh! Something happened when bringing down a container. :^(")
        return False
