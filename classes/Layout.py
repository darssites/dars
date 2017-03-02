import yaml

class Layout:

    content = []

    def __init__(self, config, site):
        with open(config, 'r') as f:
			content = yaml.load(f)

        self.content = content

        with open(self.content["css-file"], 'r') as myfile:
            css = myfile.read().replace('\n', '')

        site.appendRaw("<style>" + css + "</style>") # add the style sheet provided
        areas = self.content["areas"] # Isolate the areas in their own list
