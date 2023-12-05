def numberOfMatches(n: int) -> int:
    matches = 0

    while n != 1:
        if n % 2 == 0:
            n //= 2
            matches += n
        else:
            matches += n // 2
            n = (n // 2) + 1
    return matches
