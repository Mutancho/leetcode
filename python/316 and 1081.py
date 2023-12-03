def isPerfectSquare(num: int) -> bool:
    if num == 1:
        return True

    l, r = 1, num
    while l <= r:
        mid = l + (r-l) // 2
        pow_2 = mid * mid
        if pow_2 < num:
            l = mid + 1
        elif pow_2 > num:
            r = mid - 1
        else:
            return True
    return False

