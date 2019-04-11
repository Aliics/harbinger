import harbinger
import shutil

info_text = "Harbinger is a docker orchestration tool powered by a snakey boy."

def format_help_text():
	terminal_width = shutil.get_terminal_size().columns
	help_text = "{:<10} | {}\n".format("option", "desc")
	help_text += draw_line(terminal_width)
	for option in harbinger.OPTIONS:
		help_text += "{:<10} | {}\n".format(option["option"], option["desc"])
	return help_text

def draw_line(width, character = "="):
	line = ""
	for i in range(0, width):
		line += character
	return line

def call(param):
	try :
		print("\r\n{}\r\n\n{}".format(info_text, format_help_text()))
		return True
	except:
		return False

