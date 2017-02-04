class Header:

	text = ""
	level = 0

	def __init__(self, text, level=1):
		self.text = text
		self.level = level

	def getRaw(self):
		return "<h" + str(self.level) + ">" + str(self.text) + "</h" + str(self.level) + ">"