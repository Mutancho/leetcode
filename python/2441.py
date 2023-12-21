def findMaxK(nums: list[int]) -> int:
    unique_nums = set(nums)
    largest_val = -1
    for num in unique_nums:
        if num > 0 and -num in unique_nums and num > largest_val:
            largest_val = num
    return largest_val
