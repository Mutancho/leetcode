def minLength(s: str) -> int:
    while True:
        curr_len = len(s)
        s = s.replace("AB", "").replace("CD", "")
        new_len = len(s)
        if curr_len == new_len:
            break
    return new_len

print(minLength("ABFCACDB"))
