import os

def format_docker_images_list(docker_output):
	image_list = []
	for output in docker_output:
		fields = output.split()
		if (len(fields) > 4):
			image_list.append(
				{
					"image": fields[0],
					"version": fields[1],
					"id": fields[2],
					"mod_time": fields[3],
					"size": fields[4]
				}
			)
	return image_list

def call(param):
	try:
		docker_output = os.popen("docker images").readlines()
		images = format_docker_images_list(docker_output)
		for image in images:
			print(image)
		return True
	except:
		return False

