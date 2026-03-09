keywords = ["discipline","success","power","fear","future"]

def highlight(word):
    if word.lower() in keywords:
        return "yellow"
    return "white"