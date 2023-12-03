def reverse_vowels(s: str) -> str:
    word = list(s)
    vowels = {'a', 'e', 'i', 'o', 'u'}
    stack = []
    for ch in s:
        if ch in vowels:
            stack.append(ch)

    for i, ch in enumerate(word):
        if ch in vowels:
            word[i] = stack.pop()
    return "".join(word)
