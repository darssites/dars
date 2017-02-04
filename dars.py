import sys, os, yaml
from darssite import DarsSite
import serve

import user # the user's generation code

command = sys.argv[1]

# Open config
with open('config/config.yml', 'r') as f:
    config = yaml.load(f)

if command == "generate":
	if not os.path.exists("serve"):
		os.makedirs("serve")
	page = open('serve/index.html', 'w+')

	home = DarsSite(page, config["settings"]["title"])


if command == "serve":
	serve.serve(PORT=config["settings"]["port"])
