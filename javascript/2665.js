// class Counter {
//     constructor(init) {
//         this.count = init;
//         this.original = init
//     }
//
//     increment() {
//         return this.count++;
//     }
//
//     decrement() {
//         return this.count--;
//     }
//
//     reset() {
//         this.count = this.original
//         return this.count;
//     }
// }

var createCounter = function (init) {
    let val = init
    return {
        increment: () => ++val,
        decrement: () => --val,
        reset: () => val = init,
    }
}
