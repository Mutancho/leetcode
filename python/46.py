from itertools import permutations


def permute(nums: list[int]) -> list[list[int]]:
    return [list(x) for x in permutations(nums)]


