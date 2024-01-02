/**
 * @param {number[]} g
 * @param {number[]} s
 * @return {number}
 */
var findContentChildren = function (g, s) {
    g.sort((a, b) => a - b)
    s.sort((a, b) => a - b)
    let output = 0
    let l = g.length - 1
    let r = s.length - 1
    while (l >= 0 && r >= 0) {
        if (g[l] <= s[r]) {
            output += 1
            l -= 1
            r -= 1
        } else {
            l -= 1
        }
    }
    return output
};