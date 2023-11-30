var twoSum = function (nums, target) {
    const cache = new Map()
    for (let i = 0; i < nums.length; i++) {
        if (cache.has(target - nums[i])) {
            return [cache.get(target - nums[i]), i]
        } else {
            cache.set(nums[i], i)
        }
    }
};

console.log(twoSum([2, 7, 11, 15], 9))