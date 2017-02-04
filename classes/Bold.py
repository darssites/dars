class Bold:

	text = ""

	def __init__(self, text):
		self.text = text

	def getRaw(self):
		return "<b>" + str(self.text) + "</b>"