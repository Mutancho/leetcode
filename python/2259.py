def remove_digit(number: str, digit: str) -> str:
    max_num = -1
    digit = digit
    for i, num in enumerate(number):
        if num == digit:
            parsed_num = int(number[:i] + number[i + 1:])
            if max_num < parsed_num:
                max_num = parsed_num

    return str(max_num)
