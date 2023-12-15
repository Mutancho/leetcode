def targetIndices(nums: list[int], target: int) -> list[int]:
    output = []
    for i, v in enumerate(sorted(nums)):
        if v == target:
            output.append(i)
        if v > target:
            break

    return output

    return [i for i, v in enumerate(sorted(nums)) if v == target]
