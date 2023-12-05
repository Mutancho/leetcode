def minSum(num: int) -> int:
    nums = sorted([x for x in str(num)])
    return int(nums[0] + nums[3]) + int(nums[1] + nums[2])
