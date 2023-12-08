var sumIndicesWithKSetBits = function (nums, k) {
    let output = 0
    for (let i = 0; i < nums.length; i++) {
        let binary = i.toString(2)
        let ones = 0
        let skip = false
        for (let j = 0; j < binary.length; j++) {
            if (binary[j] === "1") {
                ones += 1
            }
            if (ones > k) {
                skip = true
                break
            }
        }
        if (!skip && ones === k) {
            output += nums[i]
        }

    }
    return output
};
console.log(sumIndicesWithKSetBits([5, 10, 1, 5, 2], 1))