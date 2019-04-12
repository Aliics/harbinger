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
	return False

def call(param):
	return True
