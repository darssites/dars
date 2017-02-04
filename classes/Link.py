class Link:

	target = ""
	text = ""
	function = ""

	def __init__(self, text, target="#", function=""):
		self.text = text
		self.target = target
		self.function = function

	def getRaw(self):
		return "<a href='" + str(self.target) + "' onclick='" + str(self.function) + "'>" + str(self.text) + "</a>"