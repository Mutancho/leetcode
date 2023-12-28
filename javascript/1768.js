/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function (word1, word2) {
    let w1_len = word1.length
    let w2_len = word2.length
    let w1_counter = 0
    let w2_counter = 0
    let output = []
    while (w1_counter < w1_len || w2_counter < w2_len) {
        if (w1_counter < w1_len) {
            output.push(word1[w1_counter])
            w1_counter += 1
        }
        if (w2_counter < w2_len) {
            output.push(word2[w2_counter])
            w2_counter += 1
        }

    }
    return output.join("")
};

console.log(mergeAlternately(word1 = "ab", word2 = "pqrs"))