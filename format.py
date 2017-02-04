def process(input):

	input = input.replace("[b]", "<b>")
	input = input.replace("[/b]", "</b>")

	input = input.replace("[i]", "<i>")
	input = input.replace("[/i]", "</i>")

	return input