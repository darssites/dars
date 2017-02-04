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
	  		<link rel="stylesheet" href="css/dars-default.css" type="text/css">
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

	def __init__(self, file, title="Moo"):
		self.file = file
		self.title = title

		self.writing = True # We can now write stuff to the file
		self.file.write(self.header.format(self.title)) # Add in title

	def append(self, obj):
		if self.writing:
			self.file.write(obj.getRaw())

	def close(self):
		self.file.write(self.footer)
		self.writing = False
