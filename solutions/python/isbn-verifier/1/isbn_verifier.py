def is_valid(isbn):
    raw_isbn = isbn.replace('-','') # clean text
    if len(raw_isbn) != 10: # too short?
        return False

    # verification
    check_sum = 0
    for i in range(len(raw_isbn)):
        if raw_isbn[i] == 'X' and i == len(raw_isbn) - 1:
            digit = '10'
        else:
            digit = raw_isbn[i] if raw_isbn[i].isdigit() else '-1'
        if digit == '-1':
            return False
        multiplier = 10 - i
        check_sum += int(digit) * multiplier
    return check_sum % 11 == 0
