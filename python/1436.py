def destCity(paths: list[list[str]]) -> str:
    destinations = {}
    for pair in paths:
        destinations[pair[0]] = pair[1]
    for pair in paths:
        if pair[1] not in destinations:
            return pair[1]

