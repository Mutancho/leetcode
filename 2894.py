def differenceOfSums(n: int, m: int) -> int:
    divisible_sum = 0
    not_divisible_sum = 0
    for i in range(1, n + 1):
        if i % m == 0:
            divisible_sum += i
        else:
            not_divisible_sum += i
    return not_divisible_sum - divisible_sum


print(differenceOfSums(10, 3))
