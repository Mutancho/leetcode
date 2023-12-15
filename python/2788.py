def splitWords(words: list[str], separator: str) -> list[str]:
    return [data for word in words for data in word.split(separator) if data]
