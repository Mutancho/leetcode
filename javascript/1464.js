/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function (nums) {
    nums.sort(function(a, b){return a - b})
    let max_len = nums.length
    return (nums[max_len - 1] - 1) * (nums[max_len - 2] - 1)
};
