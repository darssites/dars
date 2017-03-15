from utils import filter

class Link:

	target = ""
	text = ""
	function = ""

	def __init__(self, text, target="#", function=""):
		self.text = filter.filter(text)
		self.target = target
		self.function = function

	def reparse(self):
		self.text = filter.filter(self.text)

	def getRaw(self):
		return "<a href='" + str(self.target) + "' onclick='" + str(self.function) + "'>" + str(self.text) + "</a>"
