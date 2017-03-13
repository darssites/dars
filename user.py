#
# The user's code.
#

from classes.External import External
from classes.Header import Header

def code(page):

	# add bootstrap from MaxCDN
	boot = External("https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css", "stylesheet")
	page.append(boot, head=True)

	head = Header("Hello World!!!")
	page.append(head)

	# We want Bootstrap, not the default style!
	# page.addDefaultStyle()

	page.close()
