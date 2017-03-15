class Mark:

	text = ""

	def __init__(self, text):
		self.text = text

	def getRaw(self):
		return "<mark>" + str(self.text) + "</mark>"
