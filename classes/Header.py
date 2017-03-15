from utils import filter

class Header:

	text = ""
	level = 0

	def __init__(self, text, level=1):
		self.text = filter.filter(text)
		self.level = level

	def reparse(self):
		self.text = filter.filter(self.text)

	def getRaw(self):
		return "<h" + str(self.level) + ">" + str(self.text) + "</h" + str(self.level) + ">"
