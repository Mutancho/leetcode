def add_binary(a: str, b: str) -> str:
    return bin(int(a, 2) + int(b, 2))[2:]


print(add_binary("11", b="1"))
