def is_isogram(string):

    string = string.lower()

    for i in range(len(string)):
        char = string[i]
        for k in range(i + 1, len(string)):
            char2 = string[k]
            if char.isalpha() and char2.isalpha():
                if char == char2:
                    return False
    return True

