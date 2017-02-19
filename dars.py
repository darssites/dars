import sys, os, yaml
from darssite import DarsSite
import serve
import importlib

# Open config
with open('config/config.yml', 'r') as f:
    config = yaml.load(f)

import user # the user's generation code

def usage():
	print("Commands: ")
	print("- generate")
	print("- serve")
	print("- make")
	print("\nExample:")
	print("python dars.py generate")

def generate():
	print("Generating...")

	pageFile = open(config["settings"]["serveTo"] + "/index.html", "w+")

	page = DarsSite(pageFile, config["settings"]["title"])

	try:
		config["plugins"]
	except:
		print("No plugins section to your config.yml, not loading any plugins.")
		print("NOTE: If you want plugins, add this at the bottom of your config:")
		print("config:")
		print("  - plugin")
		print("  - names")
		print("  - here")
	else:
		# Load referenced plugins
		for plugin in config["plugins"]:
			print("plugin-import: " + "plugins." + plugin + "." + plugin)
			i = importlib.import_module("plugins." + plugin + "." + plugin)

			print("plugin-init: " + plugin)
			try:
				i.init(page, config)
			except:
				print("plugin-init: No init() function in " + plugin + ".py!")

	user.code(page)

if len(sys.argv) == 1:
	usage()
	sys.exit()

command = sys.argv[1]

if command == "generate":
	generate()
elif command == "make":
	generate()
	serve.serve(PORT=config["settings"]["port"])
elif command == "serve":
	serve.serve(PORT=config["settings"]["port"])
else:
	usage()