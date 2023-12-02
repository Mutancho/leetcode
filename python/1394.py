def findLucky(arr: list[int]) -> int:
    cache = {}
    max_lucky_number = -1
    for num in arr:
        if num in cache:
            cache[num] += 1
        else:
            cache[num] = 1
    for elem in cache.items():
        if elem[0] == elem[1] and elem[0] > max_lucky_number:
            max_lucky_number = elem[0]
    return max_lucky_number


