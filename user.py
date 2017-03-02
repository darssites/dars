#
# The user's code.
#

from classes.Layout import Layout

def code(page):

	columns = Layout("given-layouts/2column.yml", page)

	page.addDefaultStyle()

	page.close()
