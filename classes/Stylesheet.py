class Stylesheet:

	text = ""

	def addRule(self, appliesTo, content):
		self.text += '''
{} {{
{}
}}
		'''.format(appliesTo, content)

	def getRaw(self):
		return "<style>" + str(self.text) + "</style>"