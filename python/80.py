def removeDuplicates(nums: list[int]) -> int:
    cp = 1
    for i in range(len(nums) - 1):
        if nums[i] != nums[i + 1]:
            nums[cp] = nums[i + 1]
            cp += 1

    return cp
