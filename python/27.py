def removeElement(nums: list[int], val: int) -> int:
    counter = 0
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] != val:
            counter += 1
    return counter
    # return len(nums)


print(removeElement([3, 2, 2, 3], val=3))
