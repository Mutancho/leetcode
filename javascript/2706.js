/**
 * @param {number[]} prices
 * @param {number} money
 * @return {number}
 */
var buyChoco = function (prices, money) {
    const sorted = [...prices].sort((a, b) => a - b);
    let tm = money
    tm -= sorted[0] + sorted[1]
    if (tm >= 0) return tm
    return money
};


console.log(buyChoco([98, 54, 6, 34, 66, 63, 52, 39], 62))