import mistune

class Paragraph:

	text = ""

	def __init__(self, text):
		self.text = text
		self.text = mistune.markdown(self.text)

	def reparse(self):
		self.text = mistune.Markdown(self.text)

	def getRaw(self):
		return "<p>" + str(self.text) + "</p>"
