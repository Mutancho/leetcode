def countPoints(rings: str) -> int:
    cache = {}
    output = 0
    for i, ring in enumerate(rings):
        if i % 2 != 0:
            continue
        if rings[i + 1] not in cache:
            cache[rings[i + 1]] = {ring}
        else:
            cache[rings[i + 1]].add(ring)


    for item in cache.values():
        if len(item) == 3:
            output += 1

    return output
countPoints("B0B6G0R6R0R6G9")
