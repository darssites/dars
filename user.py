from classes.Table import Table
from classes.List import List

def code(page):

	table = Table(fullwidth=True)
	table.addHeader("Header 1", "Header 2", "Header 3", "Header 4", "Header 5")
	table.newRow()
	table.addCell("Hello", "World", "12345")
	table.newRow()
	table.addCell("I'm", "a", "table", "of", "fun!")

	page.append(table)

	list = List("Hello", "I'm", "a", "list", ordered=True)
	page.append(list)

	page.addDefaultStyle()

	page.close()