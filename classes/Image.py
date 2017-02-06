class Image:

	alt = ""
	source = ""
	scaling = ""

	def __init__(self, alt, source, width=None, height=None):
		self.alt = alt
		self.source = source

		if (width != None):
			self.scaling += "width='" + str(width) + "'"

		if (height != None):
			self.scaling += "height='" + str(height) + "'"

	def getRaw(self):

		return "<img src='" + str(self.source) + "' alt='" + str(self.alt) + "' " + str(self.scaling) + ">"