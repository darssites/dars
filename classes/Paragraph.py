from utils import filter

class Paragraph:

	text = ""

	def __init__(self, text):
		self.text = filter.filter(text)

	def reparse(self):
		self.text = filter.filter(self.text)

	def getRaw(self):
		return "<p>" + str(self.text) + "</p>"
