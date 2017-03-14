#
# The user's code.
#

from classes.Button import Button

def code(page):

	btn = Button("Visit the land of the cows!", href="http://google.com/")
	page.append(btn)

	page.addDefaultStyle()

	page.close()
