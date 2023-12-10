def transpose(matrix: list[list[int]]) -> list[list[int]]:
    # new_matrix = []
    # for i in range(len(matrix[0])):
    #     temp = []
    #     for j in range(len(matrix)):
    #         temp.append(matrix[j][i])
    #     new_matrix.append(temp)
    # return new_matrix
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
