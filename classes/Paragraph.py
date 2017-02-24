import mistune

class Paragraph:

	text = ""
	parse = False

	def __init__(self, text, markdown=False):
		self.text = text
		self.parse = markdown
		if self.parse:
			self.text = mistune.markdown(self.text)

	def reparse(self):
		self.text = mistune.Markdown(self.text)

	def getRaw(self):
		return "<p>" + str(self.text) + "</p>"
