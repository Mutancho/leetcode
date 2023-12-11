/**
 * @param {number} n
 */
var OrderedStream = function (n) {
    this.arr = new Array(n).fill(null);
    this.stored_packages = {};
};

/**
 * @param {number} idKey
 * @param {string} value
 * @return {string[]}
 */
OrderedStream.prototype.insert = function (idKey, value) {
    if (idKey !== 1) {
        for (let i = 0; i < idKey - 1; i++) {
            if (this.arr[i] === null) {
                this.stored_packages[idKey] = value
                return []
            }
        }
    }
    let output = []
    let counter = idKey
    output.push(value)
    this.arr[counter - 1] = value
    while (true) {
        counter += 1
        if (this.stored_packages[counter] === undefined) {
            return output
        }
        this.arr[counter - 1] = value
        output.push(this.stored_packages[counter])
    }
};

console.log(3 * [null])