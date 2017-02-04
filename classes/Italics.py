class Italics:

	text = ""

	def __init__(self, text):
		self.text = text

	def getRaw(self):
		return "<i>" + str(self.text) + "</i>"