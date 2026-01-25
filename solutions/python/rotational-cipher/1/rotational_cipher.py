def rotate(text, key):
    output = ""
    for char in text:
        if ord(char) >= 97:
            letter_index = (((ord(char) - 97) + key) % 26) + 97
        elif ord(char) >= 65:
            letter_index = (((ord(char) - 65) + key) % 26) + 65
        else:
            letter_index = ord(char)
        output += chr(letter_index)
    return output
