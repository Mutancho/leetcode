var findSpecialInteger = function (arr) {
    let th = arr.length / 4
    let curr_counter = 1
    let curr_num = arr[0]

    if (arr.length === 1) {
        return arr[0]
    }
    for (let i = 1; i < arr.length; i++) {
        if (curr_num === arr[i]) {
            curr_counter += 1
            if (curr_counter > th) {
                return curr_num
            }
        } else {
            curr_counter = 1
            curr_num = arr[i]
        }
    }
};