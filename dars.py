#
# dars.py
# The main program, meant as the entry point.
# Author: gusg21
#

##########################
###	  GLOBAL VERSION   ###
##########################

GLOBALVERSION = "2.6"

import sys, os, yaml
from darssite import DarsSite
import serve, packman
import importlib
import colorama

colorama.init()

# Common styles for easy use
style = {
		"error" : colorama.Fore.RED,
	 	"warning" : colorama.Fore.YELLOW,
		"success" : colorama.Fore.GREEN,
		"important" : colorama.Fore.MAGENTA,
		"reset" : colorama.Style.RESET_ALL
	}

# Open config
with open('config/config.yml', 'r') as f:
	config = yaml.load(f)

import user # the user's generation code

def usage():

	# TEXT DISPLAYED FOR HELP

	print(style["important"] + "Commands: " + style["reset"])
	print("- generate")
	print("- serve")
	print("- make")
	print("- plugins")
	print("- version")
	print("- install")
	print(style["important"] + "\nExample:" + style["reset"])
	print("python dars.py generate")

def plugins():
	# List all installed plugins

	print(style["important"] + "Installed Plugins: " + style["reset"])
	if get_immediate_subdirectories("plugins") == []:
		print(style["error"] + "No plugins found. They should be in your plugins folder." + style["reset"])
	else:
		for dir in get_immediate_subdirectories("plugins"):
			print("- " + dir)

def get_immediate_subdirectories(a_dir):
	# A little function for listing direct subdirectories.

    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

def version():
	# Print version number

	print("Dars Web framework version " + style["important"] + GLOBALVERSION + style["reset"])
	print("Written by gusg21")

def generate():
	# Generate the site. Most of the code is in darssite.py

	print(style["important"] + "Generating..." + style["reset"])

	pageFile = open(config["settings"]["serveTo"] + "/index.html", "w+")

	page = DarsSite(pageFile, config["settings"]["title"])

	try:
		config["plugins"]
	except:
		print(style["warning"] + "No plugins section to your config.yml, not loading any plugins.")
		print("NOTE: If you want plugins, add this at the bottom of your config:")
		print("config:")
		print("  - plugin")
		print("  - names")
		print("  - here" + style["reset"])
	else:
		# Load referenced plugins
		for plugin in config["plugins"]:
			print("plugin-import: " + "plugins." + plugin + "." + plugin)
			i = importlib.import_module("plugins." + plugin + "." + plugin)

			print("plugin-init: " + plugin)
			try:
				i.init(page, config)
			except:
				print(style["warning"] + "plugin-init: No init() function in " + plugin + ".py!" + style["reset"])

	user.code(page)

if len(sys.argv) == 1:
	usage()
	sys.exit()

command = sys.argv[1] # isolate the command

if command == "generate":
	generate()
elif command == "make":
	generate()
	serve.serve(PORT=config["settings"]["port"], SERVE=config["settings"]["serveTo"]) # serve from port
elif command == "serve":
	serve.serve(PORT=config["settings"]["port"], SERVE=config["settings"]["serveTo"]) # serve from port
elif command == "plugins":
	plugins()
elif command == "version":
	version()
elif command == "install":
	# run packman, see packman.py

	try:
		sys.argv[2]
	except:
		print(style["error"] + "Malformed packman command!" + style["reset"])
		print("Usage:")
		print("python dars.py install [gh user/repo OR package name]")
	else:
		packman.packman(sys.argv[2])
else:
	# otherwise, display the help
	usage()
