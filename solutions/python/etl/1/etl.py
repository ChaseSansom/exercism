def transform(legacy_data):
    data = {}
    for key, letters in legacy_data.items():
        for letter in letters:
            data[letter.lower()] = key
    return data
