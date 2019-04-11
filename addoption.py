import os
import listoption

def image_exists(image_name, images): # could gather the images internally, but this is more modular
	for image in images:
		if image["image"] == image_name:
			return True
	return False

def call(param):
	return True
