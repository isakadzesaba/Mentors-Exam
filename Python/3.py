def expend_form(number):
    num_str = str(number)
    length = len(num_str)
    expand_part = []

    for i, digit in enumerate(num_str):
        if digit != '0':
            place_value = int(digit) * (10 ** (length - i - 1))
            expand_part.append(str(place_value))

    return " + ".join(expand_part)

print(expend_form(511604))