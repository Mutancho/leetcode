/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxK = function (nums) {
    let unique_nums = new Set(nums)
    let largest_val = -1
    for (let num of unique_nums) {
        if (num > 0 && unique_nums.has(-num) && num > largest_val) {
            largest_val = num
        }
    }
    return largest_val
}
