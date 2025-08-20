def is_paired(input_string):
    open_brackets, closed_brackets, stack = '[{(', ']})', []
    for char in input_string:
        if char in open_brackets:
            stack.append(char)
        elif char in closed_brackets:
            if not stack:  # closing without an opening
                return False
            if open_brackets[closed_brackets.find(char)] != stack.pop():
                return False
    return not stack