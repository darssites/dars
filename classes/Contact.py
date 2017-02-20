import re

class Contact:

	company = ""
	phone = ""
	email = ""
	text = ""

	def __init__(self, company, phone, email, text):
		self.company = company
		self.phone = phone
		self.email = email
		self.text = text

	def getRaw(self):
		if not re.match("[^@]+@[^@]+\.[^@]+", self.email):
			composed = '''
			{}<br>
			&#9742; {}<br>
			&#9993; {}<br>
			{}<br>
			'''.format(self.company, self.phone, self.email, self.text)
		else:
			composed = '''
			{}<br>
			&#9742; {}<br>
			&#9993; <a href="mailto:{}">{}</a><br>
			{}<br>
			'''.format(self.company, self.phone, self.email, self.email, self.text)
		return "<hr><address>" + str(composed) + "</address>"
