from utils import filter

class Table():

	content = ""
	fullwidth = False

	def __init__(self, fullwidth=False):
		self.fullwidth = fullwidth

	def addCell(self, *content):
		for single in content:
			self.content += "<td>" + filter.filter(str(single)) + "</td>"

	def addHeader(self, *content):
		for single in content:
			self.content += "<th>" + filter.filter(str(single)) + "</th>"

	def newRow(self):
		self.content += "</tr><tr>"

	def getRaw(self):
		attr = ""
		if self.fullwidth:
			attr += " width='100%'"
		return "<table" + attr + "><tr>" + self.content + "</tr></table>"
