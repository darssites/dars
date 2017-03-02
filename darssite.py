#
# darssite.py
# The main class, all other classes get appended to this.
# Author: gusg21
#

import yaml, importlib

class DarsSite:

	file = None
	writing = None
	title = ""
	header = '''

	<!DOCTYPE html>
		<!--[if lte IE 6]><html class="preIE7 preIE8 preIE9"><![endif]-->
		<!--[if IE 7]><html class="preIE8 preIE9"><![endif]-->
		<!--[if IE 8]><html class="preIE9"><![endif]-->
		<!--[if gte IE 9]><!--><html><!--<![endif]-->
	  	<head>
	    	<meta charset="UTF-8">
	  		<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
	  		<meta name="viewport" content="width=device-width,initial-scale=1">
	    	<title>{}</title>

	'''

	headContent = ""

	endHead = '''
	  	</head>
	  	<body>
	'''

	internal = ""

	footer = '''
		</body>
	</html>
	'''

	def __init__(self, file, title="Moo"):
		self.file = file
		self.title = title

		self.writing = True # We can now write stuff to the file
		self.fHeader = self.header.format(self.title) # Add in title

		# Open config
		with open('config/config.yml', 'r') as f:
			config = yaml.load(f)

		try:
			config["plugins"]
		except:
			print("darssite.py: No plugins found, moving on...")
		else:
			# Load referenced plugins
			for plugin in config["plugins"]:
				i = importlib.import_module("plugins." + plugin + "." + plugin)

				print("plugin-site-init: " + plugin)
				try:
					i.site(self)
				except:
					print("plugin-init: No site() function in " + plugin + ".py!")

	def append(self, obj):
		if self.writing:
			self.internal += obj.getRaw()

	def appendRaw(self, text):
		if self.writing:
			self.internal += text

	def setTitle(self, title):
		if self.writing:
			self.fHeader = self.header.format(title)

	def addDefaultStyle(self):
		if self.writing:
			self.headContent += r'''
<style>

/* Default Dars Stylesheet */

body {

  font-size: 10pt;

  font-family: Verdana, Geneva, Arial, Helvetica, sans-serif;

  color: black;

  line-height: 14pt;

  padding-left: 5pt;

  padding-right: 5pt;

  padding-top: 5pt;

  background-color: beige;

}


h1 {

  font: 14pt Verdana, Geneva, Arial, Helvetica, sans-serif;

  font-weight: bold;

  line-height: 20pt;

}


p.subheader {

  font-weight: bold;

  color: #593d87;

}


a {

  text-decoration: none;

}


a:link, a:visited {

  color: #8094d6;

}


a:hover, a:active {

  color: #FF9933;

}


div.footer {

  font-size: 9pt;

  font-style: italic;

  line-height: 12pt;

  text-align: center;

  padding-top: 30pt;

}

table, th, td {
    border: 2px solid darkgray;
    border-collapse: collapse;
}

blockquote {
  background: #f9f9f9;
  border-left: 10px solid #ccc;
  margin: 1.5em 10px;
  padding: 0.5em 10px;
  quotes: "\201C""\201D""\2018""\2019";
}

blockquote:before {
  color: #ccc;
  content: open-quote;
  font-size: 4em;
  line-height: 0.1em;
  margin-right: 0.25em;
  vertical-align: -0.4em;
}

blockquote p {
  display: inline;
}

</style>
			'''

	def close(self):
		# Open config
		with open('config/config.yml', 'r') as f:
			config = yaml.load(f)

		# Load referenced plugins
		try:
			config["plugins"]
		except:
			pass
		else:
			for plugin in config["plugins"]:
				i = importlib.import_module("plugins." + plugin + "." + plugin)

				print("plugin-site-close: " + plugin)
				try:
					i.closesite(self)
				except:
					print("plugin-init: No closesite() function in " + plugin + ".py!")

		print("file-write: " + self.file.name)
		self.file.write(self.fHeader + self.headContent + self.endHead + self.internal + self.footer)
		self.writing = False
