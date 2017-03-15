from utils import filter

class Blockquote:

	text = ""
	cite = None

	def __init__(self, text, cite=None):
		self.text = filter.filter(text)
		self.cite = cite

	def reparse(self):
		self.text = filter.filter(self.text)

	def getRaw(self):
		if self.cite == None:
			return "<blockquote>" + str(self.text) + "</blockquote>"
		else:
			return "<blockquote cite='" + self.cite + "'><br>" + str(self.text) + "</blockquote>"
