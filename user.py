from classes.Tags import *
from classes.Stylesheet import Stylesheet
from classes.Header import Header
from classes.Rule import Rule
from classes.Paragraph import Paragraph

def code(page):

	page.setTitle("La-La-Land")

	style = Stylesheet()

	redRule = Rule("color", "red")
	underlineRule = Rule("text-decoration", "underline")
	style.addRule(getHTMLTag("Header"), redRule.text() + underlineRule.text())

	orangeRule = Rule("color", "orange")
	style.addRule(getHTMLTag("Paragraph"), orangeRule.text())

	page.append(style)

	page.addDefaultStyle()

	title = Header("Moo")
	page.append(title)

	text = Paragraph("Hello World. I'm a paragraph.")
	page.append(text)

	page.close()