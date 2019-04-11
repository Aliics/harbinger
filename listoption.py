import os

def format_docker_images_list(docker_output):
	image_list = []
	for output in docker_output:
		fields = output.split()
		if (len(fields) == 7):
			image_list.append(
				{
					"image": shorten_image_name(fields[0]),
					"version": fields[1],
					"id": fields[2],
					"mod_time": "{} {} {}".format(fields[3], fields[4], fields[5]),
					"size": fields[6]
				}
			)
	return image_list

def shorten_image_name(long_name):
	name_dirs = long_name.split("/")
	last_index = len(name_dirs) - 1 if len(name_dirs) > 0 else 0
	return name_dirs[last_index]

def beautify_docker_image_dict(docker_images):
	beautiful_grid = "image           | version                   | id              | mod_time        | size           \n" if not len(docker_images) == 0 else ""
	for row in docker_images:
		beautiful_grid += "{:15.15} | {:25.25} | {:15.15} | {:15.15} | {:15.15}\n".format(row["image"], row["version"], row["id"], row["mod_time"], row["size"])
		
	return beautiful_grid

def call(param):
	try:
		docker_output = os.popen("docker images").readlines()
		output = beautify_docker_image_dict(format_docker_images_list(docker_output))
		print(output)
		return True
	except:
		return False

