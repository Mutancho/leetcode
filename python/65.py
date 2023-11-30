def valid_number(s: str) -> bool:
    try:
        int(s)
        return True
    except:
        return False

print(valid_number("e"))