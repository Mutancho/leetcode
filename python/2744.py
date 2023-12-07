def maximumNumberOfStringPairs(words: list[str]) -> int:
    pairs = {}
    output = 0

    for word in words:
        if word not in pairs and word[::-1] not in pairs:
            pairs[word] = 1
        else:
            output += 1
    return output
