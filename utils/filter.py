import mistune

# Text given to classes FOR DISPLAY should be filtered through here.
def filter(text):
    # parse MD
    text = mistune.markdown(text)
    # Strip <p></p>
    # text = text[3:-4] # remove <p> (3:), remove </p> (:-4)
    return text
