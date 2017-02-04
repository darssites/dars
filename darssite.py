import format

class DarsSite:

	file = None
	writing = None
	title = "Flubbadee-Fish"
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
	  	</head>
	  	<body>
	'''

	footer = '''
		</body>
	</html>
	'''

	def __init__(self, file, title):
		self.file = file
		self.title = title

		self.writing = True # We can now write stuff to the file
		self.file.write(self.header.format(title)) # Add in title

	def newHeader(self, text, level):
		text = format.process(text)

		if self.writing:
			self.file.write("<h" + str(level) + ">" + str(text) + "</h" + str(level) + ">")

	def newParagraph(self, text):
		text = format.process(text)

		if self.writing:
			self.file.write("<p>" + str(text) + "</p>")

	def close(self):
		self.file.write(self.footer)
		self.writing = False
