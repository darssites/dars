class Scripted:

	text = ""
	type = ""

	def __init__(self, text, type="superscript"):
		if type != "superscript" and type != "subscript":
			print("Invalid Script type: " + type)
			print("Setting to superscript...")
			self.type = "superscript"
		else:
			self.type = type

		self.text = text

	def getRaw(self):
		if self.type == "superscript":
			aType = "sup"
		if self.type == "subscript":
			aType = "sub"
		return "<" + aType + ">" + str(self.text) + "</" + aType + ">"