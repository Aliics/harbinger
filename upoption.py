import os


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
    try:
        os.system("docker run {}".format(image_name))
        return True
    except:
        return False


def call(param):
    try:
        added_images = list_added_images(".added_images")
        if len(added_images) == 0:
            print("Nice try! There are no containers to bring up. ;^)")
            return True
        for added_image in added_images:
            run_docker_container(added_image)
        return True
    except:
        return False
