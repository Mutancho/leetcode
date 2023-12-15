def finalString(s: str) -> str:
    output = []
    for ch in s:
        if ch != "i":
            output.append(ch)
        else:
            output.reverse()
    return "".join(output)
