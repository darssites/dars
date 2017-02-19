class Blockquote:

	text = ""
	cite = None

	def __init__(self, text, cite=None):
		self.text = text
		self.cite = cite

	def getRaw(self):
		if self.cite == None:
			return "<blockquote>" + str(self.text) + "</blockquote>"
		else:
			return "<blockquote cite='" + self.cite + "'><br>" + str(self.text) + "</blockquote>"