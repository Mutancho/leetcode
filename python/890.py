def findAndReplacePattern(words: list[str], pattern: str) -> list[str]:
    output = []
    for word in words:
        cache = {}
        for i, v in enumerate(word):
            if pattern[i] not in cache:
                if v not in cache.values():
                    cache[pattern[i]] = v
                else:
                    break
            else:
                if cache[pattern[i]] != v:
                    break
        else:
            output.append(word)
    return output



