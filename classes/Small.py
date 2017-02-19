class Small:

	text = ""

	def __init__(self, text):
		self.text = text

	def getRaw(self):
		return "<small>" + str(self.text) + "</small>"