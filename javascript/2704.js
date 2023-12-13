/**
 * @param {string} val
 * @return {Object}
 */
var expect = function (val) {
    return {
        toBe: (new_val) => {
            if (val === new_val) return true;
            else throw new Error("Not Equal");
        },
        notToBe: (new_val) => {
            if (val !== new_val) return true;
            else throw new Error("Equal");
        }
    }
};
