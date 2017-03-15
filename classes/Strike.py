from utils import filter

class Strike:

	text = ""

	def __init__(self, text):
		self.text = filter.filter(text)

	def reparse(self):
		self.text = filter.filter(self.text)

	def getRaw(self):
		return "<del>" + str(self.text) + "</del>"
