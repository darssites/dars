from utils import filter

class Anchor:

	text = ""
	name = ""

	def __init__(self, text, name):
		self.text = filter.filter(text)
		self.name = name

	def reparse(self):
		self.text = filter.filter(self.text)

	def getRaw(self):
		return "<a id=" + str(self.name) + ">" + str(self.text) + "</a>"
