def answer(question):
    tokens = question.strip("!.?").split()

    q_operations = [term for term in tokens if term in ("plus", "minus", "multiplied", "divided", "squared", "cubed")]
    q_numbers = [int(term) for term in tokens if term.lstrip('-').isnumeric()]

    if not q_numbers:
        raise ValueError("syntax error")

    # Validate that meaningful tokens alternate: number, op, number, op ...
    meaningful = [t for t in tokens if t.lstrip('-').isnumeric() or t in ("plus", "minus", "multiplied", "divided", "squared", "cubed")]
    for i, t in enumerate(meaningful):
        is_num = t.lstrip('-').isnumeric()
        if i % 2 == 0 and not is_num:
            raise ValueError("syntax error")
        if i % 2 == 1 and is_num:
            raise ValueError("syntax error")

    ans = q_numbers.pop(0)

    if q_operations:
        try:
            for op in q_operations:
                match op:
                    case "plus":
                        ans += q_numbers.pop(0)
                    case "minus":
                        ans -= q_numbers.pop(0)
                    case "multiplied":
                        ans *= q_numbers.pop(0)
                    case "divided":
                        ans //= q_numbers.pop(0)
                    case _:
                        raise ValueError("unknown operation")
        except IndexError:
            raise ValueError("syntax error")

    if q_numbers:
        raise ValueError("syntax error")

    return ans