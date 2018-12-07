def reverse(text):
    new_string = ""
    for i in reversed(range(len(text))):
        new_string = new_string + text[i]
    return new_string
