def frequencySort(s: str) -> str:
    return "".join([key[0] * key[1] for key in sorted({ch: s.count(ch) for ch in set(s)}.items(), key=lambda item: item[1], reverse=True)])



print(frequencySort("tree"))
