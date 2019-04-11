import harbinger

info_text = "Harbinger is a docker orchestration tool power by a snakey boy."

def format_help_text():
	help_text = "{:<10} | {}\n".format("option", "desc")
	help_text += "=================================================================================================================================================\n"
	for option in harbinger.OPTIONS:
		help_text += "{:<10} | {}\n".format(option["option"], option["desc"])
	return help_text

def call(param):
	try :
		print("\r\n{}\r\n\n{}".format(info_text, format_help_text()))
		return True
	except:
		return False

