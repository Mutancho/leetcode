def rotate(nums: list[int], k: int) -> None:
    k = len(nums) - (k % len(nums))
    nums[:] = nums[k:] + nums[:k]

