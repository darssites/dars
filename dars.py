#
# dars.py
# The main program, meant as the entry point.
# Author: gusg21
#

##########################
###	  GLOBAL VERSION   ###
##########################

GLOBALVERSION = "2.7"

import sys, os, yaml, argparse
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
		print(style["warning"] + "No plugins section to your config.yml, not loading any plugins." + style["reset"])
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

parser = argparse.ArgumentParser(description="The controller for dars. http://github.com/darssites/dars")
parser.add_argument("--generate", action="store_true", help="Generate the site")
parser.add_argument("--make", action="store_true", help="Generate and serve the site")
parser.add_argument("--serve", action="store_true", help="Serve the site on localhost")
parser.add_argument("--plugins", action="store_true", help="List all installed plugins")
parser.add_argument("--version", action="store_true", help="Display dars' version number")
parser.add_argument("--install", dest="package", help="Download a package to the current project")

args = parser.parse_args()

if args.generate:
	generate()
elif args.make:
	generate()
	serve.serve(PORT=config["settings"]["port"], SERVE=config["settings"]["serveTo"]) # serve from port
elif args.serve:
	serve.serve(PORT=config["settings"]["port"], SERVE=config["settings"]["serveTo"]) # serve from port
elif args.plugins:
	plugins()
elif args.version:
	version()
elif args.package:
	packman.packman(args.package)
