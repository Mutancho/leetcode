def myAtoi(s: str) -> int:
    strings = s.split(" ")
    for string in strings:
        try:
            return int(string)
        except:
            continue




print(myAtoi(s="-0042"))
