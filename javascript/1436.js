var destCity = function (paths) {
    const cache_destination = new Map()
    for (let i = 0; i < paths.length; i++) {
        cache_destination.set(paths[i][0], paths[i][1])
    }
    for (let i = 0; i < paths.length; i++) {
        if (!cache_destination.get(paths[i][1])) {
            return paths[i][1]
        }
    }
}

console.log(destCity([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]))