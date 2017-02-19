from classes.Blockquote import Blockquote

def code(page):

	quote = Blockquote('''
		Hello. I'm a quote that isn't REALLY a quote, but you know...<br>
		I can also span<br>
		many<br>
		many<br>
		MANY<br>
		lines!<br>
		<br>
		<br>
		<br>
		<br>
		<br>
		<br>
		<br>
		Even infinite!
		''', cite="Zeus")
	page.append(quote)

	page.addDefaultStyle()

	page.close()
