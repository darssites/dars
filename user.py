from classes.Paragraph import Paragraph
from classes.Italics import Italics
from classes.Link import Link
from classes.Header import Header
from classes.Code import Code
from classes.JScript import JScript

def code(page):

	title = Header("Your Dars Site")
	page.append(title)

	js = JScript('''
		function disp() {
			alert("Hello World!")
		}
		''')
	page.append(js)

	world = Italics("World")
	para = Paragraph("Hello " + world.getRaw())
	page.append(para)

	linkTest = Link("Click me", function="disp()")
	page.append(linkTest)

	page.close()