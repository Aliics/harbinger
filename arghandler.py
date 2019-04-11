import sys
import harbinger

valid_options = harbinger.OPTIONS 

def arg_options_dict(args):
	options = []
	for i in range(0, len(args)):
		option = args[i]
		if option_is_valid(option):
			param = args[i + 1] if len(args) > i + 1 else ""
			options.append({"option": option})
			if not param == "" and option_req_param(option):
				options[len(options) - 1]["param"] = param
	return options	

def option_is_valid(option):
	for valid_option in valid_options:
		if option == valid_option["option"]:
			return True
	return False

def option_req_param(option):
	for valid_option in valid_options:
		if option == valid_option["option"]:
			return valid_option["requires_param"]
	return False

# I decided to make this return the execution state
# Should make it easier to write unit tests
def handle_given_options(options):
	execution = True
	for option in options:
		found = False
		for valid_option in valid_options:
			if option["option"] == valid_option["option"]:
				found = True
				execution = valid_option["call"](option["param"] if "param" in option else "" )
				if execution: 
					continue 
				else: 
					break
		if not found:
			execution = False
			break
	return execution

