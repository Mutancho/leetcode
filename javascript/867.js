var transpose = function (matrix) {
    let new_matrix = []
    for (let i = 0; i < matrix[0].length; i++) {
        let temp = []
        for (let j = 0; j < matrix.length; j++) {
            temp.push(matrix[j][i])
        }
        new_matrix.push(temp)
    }
    return new_matrix
};