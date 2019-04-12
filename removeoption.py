def image_is_added(image_name, file_name):
	try: 
		added_images = open(file_name, "r")
		images = added_images.readlines()
		for image in images:
			if image_name == image.rstrip():
				added_images.close()
				return True
		added_images.close()
	except:
		return False

def remove_added_image(image_name, file_name):
	if image_is_added(image_name, file_name):
		added_images = open(file_name, "r")
		images = added_images.readlines()
		added_images.close()
		new_images = []
		for image in images:
			if not image_name == image.rstrip():
				new_images.append(image)
			else:
				print("Image [{}] has been cleanly removed from your cluster.".format(image_name))
		added_images = open(file_name, "w")
		added_images.writelines(new_images)
		added_images.close()
	else:
		print("Image [{}] is not in your cluster at all!".format(image_name))

def call(param):
	try:
		remove_added_image(param, ".added_images")
		return True
	except:
		return False

