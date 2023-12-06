var totalMoney = function (n) {
    let output = 0
    let max_weeks = Math.ceil(n / 7)
    for (let i = 1; i < max_weeks + 1; i++) {
        for (let j = i; j < i + 7; j++) {
            output += j
            n -= 1
            if (n === 0) {
                break
            }
        }
    }
    return output
};