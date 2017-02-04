class Paragraph:

	text = ""

	def __init__(self, text):
		self.text = text

	def getRaw(self):
		return "<p>" + str(self.text) + "</p>"