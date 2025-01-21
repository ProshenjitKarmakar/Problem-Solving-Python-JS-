/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function (functions) {
    return (input) => {
        return functions.reduceRight((acc, fn) => {
            return fn(acc);
        }, input);
    };
};

const fn = compose([x => x + 1, x => 2 * x])
const res = fn(4)
console.log("======res===", res);

