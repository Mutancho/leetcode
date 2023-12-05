var numberOfMatches = function (n) {
    let matches = 0

    while (n !== 1) {
        if (n % 2 === 0) {
            n = Math.floor(n / 2)
            matches += n
        } else {
            matches += Math.floor(n / 2)
            n = Math.floor(n / 2) + 1
        }
    }
    return matches
};
console.log(numberOfMatches(7))