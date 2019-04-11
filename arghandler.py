import sys
import helpfunc

valid_options = [
	{
		"option": "--help",
		"requires_param": False,
	},
	{
		"option": "--version",
		"requires_param": False
	},
	{
		"option": "--list",
		"requires_param": False
	},
	{
		"option": "--add",
		"requires_param": True
	}
]

option_functions = {
	"--help": helpfunc.call
}

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
		for k, v in option_functions.items():
			if option["option"] == k:
				execution = v(option["param"] if "param" in option else "" )
				if execution: continue 
				else: break
	return execution

