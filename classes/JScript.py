class JScript:

	text = ""

	def __init__(self, text):
		self.text = text

	def getRaw(self):
		return "<script>" + str(self.text) + "</script>"