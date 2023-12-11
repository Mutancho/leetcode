def findSpecialInteger(arr: list[int]) -> int:
    th = len(arr) / 4
    curr_counter = 1
    curr_num = arr[0]
    if len(arr) == 1:
        return arr[0]
    for i in range(1, len(arr)):
        if curr_num == arr[i]:
            curr_counter += 1
            if curr_counter > th:
                return curr_num
        else:
            curr_counter = 1
            curr_num = arr[i]
