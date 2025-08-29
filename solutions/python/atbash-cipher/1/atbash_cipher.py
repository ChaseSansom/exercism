def encode(plain_text):
    cleaned = ''.join(ch.lower() for ch in plain_text if ch.isalnum())
    out = []
    for i, ch in enumerate(cleaned, start=1):
        out.append(ciphered_char(ch))
        if i % 5 == 0 and i != len(cleaned):  # no trailing space
            out.append(' ')
    return ''.join(out)

def decode(ciphered_text):
    cleaned = ''.join(ch.lower() for ch in ciphered_text if ch.isalnum())
    return ''.join(ciphered_char(ch) for ch in cleaned)

def ciphered_char(char):
    cipher = 'zyxwvutsrqponmlkjihgfedcba'
    if char.isalpha():
        return cipher[ord(char.lower()) - ord('a')]
    return char