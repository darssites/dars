#
# The user's code.
#

from classes.Anchor import Anchor
from classes.Link import Link
from classes.Paragraph import Paragraph

def code(page):

	toAnchor = Link("Jump to Anchor", target="#anchor")
	page.append(toAnchor)

	newlines = Paragraph("<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>")
	page.append(newlines)

	anchor1 = Anchor("I'm an anchor!", "anchor")
	page.append(anchor1)

	page.addDefaultStyle()

	page.close()
