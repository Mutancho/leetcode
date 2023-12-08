def decode(encoded: list[int], first: int) -> list[int]:
    output = [first]
    for num in encoded:
        output.append(output[-1] ^ num)
    return output
