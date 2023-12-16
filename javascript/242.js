/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
    if (s.length !== t.length) {
        return false
    }
    let s_cache = {}
    let t_cache = {}
    for (let i = 0; s.length > i; i++) {
        let curr_s_letter = s[i]
        let curr_t_letter = t[i]
        if (!s_cache.hasOwnProperty(curr_s_letter)) {
            s_cache[curr_s_letter] = 1
        } else {
            s_cache[curr_s_letter] += 1
        }
        if (!t_cache.hasOwnProperty(curr_t_letter)) {
            t_cache[curr_t_letter] = 1
        } else {
            t_cache[curr_t_letter] += 1
        }
    }

    for (let char of s) {
        if (s_cache[char] !== t_cache[char]) {
            return false
        }
    }
    return true
};

console.log(isAnagram(s = "aacc", t = "ccac"))