def findWordsContaining(words: list[str], x: str) -> list[int]:
    return [i for i, v in enumerate(words) if x in v]


print(findWordsContaining(words=["abc", "bcd", "aaaa", "cbc"], x="a"))
