from collections import Counter


def findTheDifference(s: str, t: str) -> str:
    return next(pair[0] for pair in Counter(s + t).items() if pair[1] % 2 != 0)
