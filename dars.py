import sys, os, yaml
from darssite import DarsSite
import serve

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

	if not os.path.exists(config["settings"]["serveTo"]):
		os.makedirs(config["settings"]["serveTo"])
		print("Creating serve directory...")
	else:
		print("Located serve directory, moving on...")
	pageFile = open('serve/index.html', 'w+')

	page = DarsSite(pageFile, config["settings"]["title"])

	user.code(page)

if len(sys.argv) == 1:
	usage()
	sys.exit()

command = sys.argv[1]

# Open config
with open('config/config.yml', 'r') as f:
    config = yaml.load(f)

if command == "generate":
	generate()


if command == "make":
	generate()
	serve.serve(PORT=config["settings"]["port"])


if command == "serve":
	serve.serve(PORT=config["settings"]["port"])