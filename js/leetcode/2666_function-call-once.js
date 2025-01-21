/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function (fn) {
    let called = false;
    let result;

    return function (...args) {
        if (!called) {
            result = fn(...args); // Call fn with arguments
            called = true;
            return result; // Return the result of fn
        }
        return undefined; // Return undefined on subsequent calls
    };
};

let fn = (a, b, c) => (a + b + c)
let onceFn = once(fn)
const res1 = onceFn(1, 2, 3); // 6
const res2 = onceFn(2, 3, 6); // returns undefined without calling fn


console.log("====res1======", res1);
console.log("====res2======", res2);




