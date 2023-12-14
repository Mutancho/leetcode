def onesMinusZeros(grid: list[list[int]]) -> list[list[int]]:
    def get_col_sum(mat: list[list[int]], x: int, y: int) -> tuple[int, int]:
        temp_x = x
        col_sum_one = 0
        col_sum_zero = 0
        while temp_x >= 0:
            curr = mat[temp_x][y]
            if curr == 1:
                col_sum_one += 1
            else:
                col_sum_zero += 1
            temp_x -= 1

        temp_x = x + 1

        while temp_x < len(mat):
            curr = mat[temp_x][y]
            if curr == 1:
                col_sum_one += 1
            else:
                col_sum_zero += 1
            temp_x += 1

        return col_sum_one, col_sum_zero

    new_matrix = [[None for _ in range(len(grid[0]))] for j in range(len(grid))]
    cache_row_sum = {}
    cache_col_sum = {}

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i not in cache_row_sum:
                sum_gird_i = sum(grid[i])
                cache_row_sum[i] = sum_gird_i - (len(grid[i]) - sum_gird_i)
            row_sum = cache_row_sum[i]

            if j not in cache_col_sum:
                col_sum_ones, col_sum_zeroes = get_col_sum(grid, i, j)
                cache_col_sum[j] = col_sum_ones - col_sum_zeroes
            col_sum = cache_col_sum[j]

            new_matrix[i][j] = row_sum + col_sum
    return new_matrix
