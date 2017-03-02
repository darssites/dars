#
# The user's code.
#

from classes.Paragraph import Paragraph

def code(page):

	text = Paragraph("Mooooooo!")
	page.append(text)

	page.addDefaultStyle()

	page.close()
