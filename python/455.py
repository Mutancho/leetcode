def findContentChildren(g: list[int], s: list[int]) -> int:
    g.sort()
    s.sort()
    output = 0
    l, r = len(g) - 1, len(s) - 1
    while l >= 0 and r >= 0:
        if g[l] <= s[r]:
            output += 1
            l -= 1
            r -= 1
        else:
            l -= 1
    return output


print(findContentChildren(g=[1, 2], s=[1, 2, 3]))
