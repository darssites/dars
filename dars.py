import sys, os, yaml
from darssite import DarsSite
import serve
import importlib
import colorama

colorama.init()

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
	print(style["important"] + "Commands: " + style["reset"])
	print("- generate")
	print("- serve")
	print("- make")
	print("- plugins")
	print(style["important"] + "\nExample:" + style["reset"])
	print("python dars.py generate")

def plugins():
	print(style["important"] + "Installed Plugins: " + style["reset"])
	if get_immediate_subdirectories("plugins") == []:
		print(style["error"] + "No plugins found. They should be in your plugins folder." + style["reset"])
	else:
		for dir in get_immediate_subdirectories("plugins"):
			print("- " + dir)

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

def generate():
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

command = sys.argv[1]

if command == "generate":
	generate()
elif command == "make":
	generate()
	serve.serve(PORT=config["settings"]["port"])
elif command == "serve":
	serve.serve(PORT=config["settings"]["port"])
elif command == "plugins":
	plugins()
else:
	usage()
