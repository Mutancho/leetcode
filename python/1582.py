
def numSpecial(mat: list[list[int]]) -> int:
    def is_row_special_func(row: list) -> tuple[bool | None, int]:
        is_special = None
        idx = 0
        for elem_idx in range(len(row)):
            if row[elem_idx] == 1:
                if is_special is not True:
                    is_special = True
                    idx = elem_idx
                else:
                    return False, 0
        return is_special, idx

    def is_vertical_special_func(mat: list[list[int]], x, y) -> bool:
        t_x = x - 1
        while 0 <= t_x:
            if mat[t_x][y] == 1:
                return False
            t_x -= 1
        t_x = x + 1
        while t_x < len(mat):
            if mat[t_x][y] == 1:
                return False
            t_x += 1
        return True
    output = 0
    for i in range(len(mat)):
        is_row_special, y_idx = is_row_special_func(mat[i])
        if not is_row_special:
            continue
        is_vertical_special = is_vertical_special_func(mat, i, y_idx)
        if is_vertical_special:
            output += 1
    return output




print(numSpecial([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
