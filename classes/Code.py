class Code:

	text = ""

	def __init__(self, text):
		self.text = text

	def getRaw(self):
		return "<code>" + str(self.text) + "</code>"