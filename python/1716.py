import math


def totalMoney(n: int) -> int:
    output = 0
    max_weeks = math.ceil(n / 7)
    for i in range(1, max_weeks + 1):
        for j in range(i, i + 7):
            output += j
            n -= 1
            if n == 0:
                break
    return output
