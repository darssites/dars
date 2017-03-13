class External:

	location = ""
	rel = ""

	def __init__(self, location, rel):
		self.location = location
		self.rel = rel

	def getRaw(self):
		return "<link href='" + self.location + "' rel='" + self.rel + "' />"
