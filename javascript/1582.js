/**
 * @param {number[][]} mat
 * @return {number}
 */
var numSpecial = function (mat) {
    var isRowSpecialFunc = function (row) {
        let isSpecial = null
        let idx = 0
        for (let i = 0; i < row.length; i++) {
            if (row[i] === 1) {
                if (isSpecial !== true) {
                    isSpecial = true
                    idx = i
                } else {
                    return [false, 0]
                }
            }
        }
        return [isSpecial, idx]
    }
    var isColVerticalSpecialFunc = function (mat, x, y) {
        let tX = x - 1
        while (0 <= tX) {
            if (mat[tX][y] === 1) {
                return false
            }
            tX -= 1
        }
        tX = x + 1
        while (tX < mat.length) {
            if (mat[tX][y] === 1) {
                return false
            }
            tX += 1
        }
        return true
    }
    let output = 0
    for (let i = 0; i < mat.length; i++) {
        let [isRowSpecial, yIdx] = isRowSpecialFunc(mat[i])
        if (!isRowSpecial) {
            continue
        }
        let isVerticalSpecial = isColVerticalSpecialFunc(mat, i, yIdx)
        if (isVerticalSpecial) {
            output += 1
        }
    }
    return output
};

console.log(numSpecial([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))