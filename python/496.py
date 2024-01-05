def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    cache = {v: i for i, v in enumerate(nums2)}
    output = []
    for j, num in enumerate(nums1):
        output.append(next((nums2[i] for i in range(cache[num] + 1, len(nums2)) if num < nums2[i]), -1))
    return output

