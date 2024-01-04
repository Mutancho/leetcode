def minOperations(nums: list[int]) -> int:
    cache = {}
    arr_len = len(nums)
    output = 0
    for num in nums:
        if num not in cache:
            cache[num] = 1
        else:
            cache[num] += 1
    for val in cache.values():
        while val >= 1:
            if val >= 5:
                val -= 3
                arr_len -= 3
            elif val == 4:
                val -= 2
                arr_len -= 2
            elif val == 3:
                val -= 3
                arr_len -= 3
            elif val == 2:
                val -= 2
                arr_len -= 2
            elif val == 1:
                return - 1
            output += 1

    return output


print(minOperations([2, 1, 2, 2, 3, 3]))
