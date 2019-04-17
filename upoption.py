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


def call(param):
    return True
