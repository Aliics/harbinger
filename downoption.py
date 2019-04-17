import os
import upoption
from multiprocessing import Process


def run_docker_container(image_name):
    os.popen("docker stop {}".format(image_name)).close()


def call(param):
    try:
        added_images = upoption.list_added_images(".added_images")
        if len(added_images) == 0:
            print("Nice try! There are no containers to bring up. ;^)")
            return True
        processes = []
        for added_image in added_images:
            docker_runner = Process(target=run_docker_container, args=(added_image,))
            docker_runner.start()
            processes.append(docker_runner)
        for process in processes:
            process.join()
        return True
    except:
        print("Uh oh! Something happened when bringing up a container. :^(")
        return False
