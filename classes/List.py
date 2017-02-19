class List:

	content = ""
	ordered = False
	type = ""

	def __init__(self, *items, ordered=False, type="square"):
		self.ordered = ordered
		self.type = type

		for item in items:
			self.content += "<li>" + item + "</li>"

	def getRaw(self):
		if self.ordered:
			return "<ol type='" + self.type + "'>" + self.content + "</ol>"
		else:
			return "<ul style='list-style-type:" + self.type + "'>" + self.content + "</ul>"