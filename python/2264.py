def largestGoodInteger(num: str) -> str:
    tc = 1
    curr_max = -1
    for i in range(1, len(num)):
        if num[i] == num[i - 1]:
            tc += 1
            if tc == 3 and int(num[i]) > curr_max:
                curr_max = int(num[i])
        else:
            tc = 1
    return "" if curr_max == -1 else str(curr_max) * 3


print(largestGoodInteger("2300019"))
