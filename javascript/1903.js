var largestOddNumber = function (num) {
    for (let i = num.length - 1; 0 <= i; i--) {
        if (["1", "3", "5", "7", "9"].includes(num[i])) {
            return num.slice(0, i + 1)
        }
    } return ""
};

console.log(largestOddNumber("52"))