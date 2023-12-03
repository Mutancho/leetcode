class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        for i in range(1, len(nums)):
            nums[i] = nums[i - 1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right] + self.nums[left]
