def setZeroes(matrix: list[list[int]]):
    zeroes = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                zeroes.append([i, j])
    for zero in zeroes:
        matrix[zero[0]] = [0] * len(matrix[0])
        up, down = zero[0], zero[0]
        while up >= 0:
            matrix[up][zero[1]] = 0
            up -= 1
        while down < len(matrix):
            matrix[down][zero[1]] = 0
            down += 1
    return matrix


