def digitSum(s: str, k: int) -> str:
    while len(s) > k:
        new_s = ""
        for i in range(0, len(s), k):
            chunk = s[i:i + k]
            chunk_sum = 0
            for digit in chunk:
                chunk_sum += int(digit)
            new_s += str(chunk_sum)
        s = new_s

    return s
