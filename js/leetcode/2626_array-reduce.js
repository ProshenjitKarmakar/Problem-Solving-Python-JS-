/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */

function sum(accum, curr) { return accum + curr; }
// function sum(accum, curr) { return accum + curr * curr; }

var reduce = function (nums, fn, init) {
        let current = init

        for (let i = 0; i < nums.length; i++) {
            current = fn(current, nums[i])
        }

        return current
};

const res = reduce([1, 2, 3, 4], sum, 0)

console.log("======res======", res);

