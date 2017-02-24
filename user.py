#
# The user's code.
#

from classes.Paragraph import Paragraph

def code(page):

	mdText = Paragraph("Hey, **that's** pretty _awesome_!", markdown=True)
	page.append(mdText)

	page.addDefaultStyle()

	page.close()
