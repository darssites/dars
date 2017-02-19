class Strike:

	text = ""

	def __init__(self, text):
		self.text = text

	def getRaw(self):
		return "<del>" + str(self.text) + "</del>"