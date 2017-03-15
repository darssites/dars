#
# The user's code.
#

from classes.Paragraph import Paragraph
from classes.Button import Button
from classes.Contact import Contact
from classes.Anchor import Anchor
from classes.Blockquote import Blockquote
from classes.Header import Header
from classes.Link import Link
from classes.List import List
from classes.Mark import Mark
from classes.Small import Small
from classes.Table import Table
from classes.Strike import Strike

def code(page):

	para = Paragraph("New, **tasty**, _filtering_!")
	page.append(para)

	btn = Button("I can _filter_!")
	page.append(btn)

	contact = Contact("Blah Inc.", "bla-hbl-ahbl", "blah@blah.blah", "I can **filter**!")
	page.append(contact)

	anchor = Anchor("Text _filtering_!", "blah")
	page.append(anchor)

	quote = Blockquote("I can filter **too**!")
	page.append(quote)

	head = Header("It's not even _special_ anymore!")
	page.append(head)

	link = Link("Whee**e**_e_**e**!", target="http://google.com/")
	page.append(link)

	list = List("Hello", "I'm", "in", "a", "**list**")
	page.append(list)

	sm = Small("Teeny, tiny **text**!")
	page.append(sm)

	table = Table(fullwidth=True)
	table.addHeader("Header", "_Header_", "Header")
	table.newRow()
	table.addCell("Item", "_Item_", "Item")
	page.append(table)

	strike = Strike("Hello _World_!")
	page.append(strike)

	page.addDefaultStyle()

	page.close()
