class Anchor:

	text = ""
	name = ""

	def __init__(self, text, name):
		self.text = text
		self.name = name

	def getRaw(self):
		return "<a id=" + str(self.name) + ">" + str(self.text) + "</a>"