def medianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    import statistics
    return statistics.median(nums1 + nums2)


print(medianSortedArrays(nums1 = [1,2], nums2 = [3,4]))

