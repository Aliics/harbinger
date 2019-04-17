import os
from multiprocessing import Process


def list_added_images(file_name):
    try:
        added_images = open(file_name, "r")
        images = added_images.readlines()
        added_images.close()
        trim_images = []
        for image in images:
            trim_images.append(image.rstrip())
        return trim_images
    except FileNotFoundError:
        return []


def run_docker_container(image_name):
    os.popen("docker run --detach {}".format(image_name)).close()


def call(param):
    try:
        added_images = list_added_images(".added_images")
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
