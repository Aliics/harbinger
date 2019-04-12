import os
import listoption

def image_exists(image_name, images): # could gather the images internally, but this is more modular
	for image in images:
		if image["image"] == image_name:
			return True
	return False

def file_contains_image(image_name, file_name):
	try:
		added_images_file = open(file_name, "r")
		images = added_images_file.readlines()
		for image in images:
			image_name_escaped = "{}\n".format(image_name)
			if image_name_escaped == image:
				added_images_file.close()
				return True
		added_images_file.close()
	except:
		return False
	return False

def append_image_to_file(image_name, file_name):
	added_images_file = open(file_name, "a")
	if not file_contains_image(image_name, file_name):
		added_images_file.write("{}\n".format(image_name))
	added_images_file.close()

def call(param):
	docker_output = os.popen("docker images").readlines()
	images = listoption.format_docker_images_list(docker_output)
	image = param.rstrip()
	if image_exists(image, images):
		append_image_to_file(image, ".added_images")
	return True
