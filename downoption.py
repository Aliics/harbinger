import os
import upoption
from multiprocessing import Process


def list_container_ids(added_images, current_containers):
    container_ids = []
    for current_container in current_containers:
        current_details = current_container.split()
        if len(current_details) > 6:
            container_id = current_details[0]
            container_name = current_details[1]
            for added_image in added_images:
                if container_name == added_image:
                    container_ids.append(container_id)
                    break
    return container_ids


def stop_docker_container(container_id):
    os.system("docker stop {}".format(container_id))


def call(param):
    try:
        added_images = upoption.list_added_images(".added_images")
        current_containers = list_container_ids(added_images, os.popen("docker ps").readlines())
        if len(current_containers) == 0:
            print("Nice try! There are no containers even in the cluster. ;^)")
            return True
        print("Containers stopped:")
        processes = []
        for current_container in current_containers:
            docker_runner = Process(target=stop_docker_container, args=(current_container,))
            docker_runner.start()
            processes.append({current_container, docker_runner})
        for container_id, process in processes:
            process.join()

        return True
    except:
        print("Uh oh! Something happened when bringing down a container. :^(")
        return False
