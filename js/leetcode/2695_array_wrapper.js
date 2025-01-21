/**
 * @param {number[]} nums
 * @return {void}
 */
var ArrayWrapper = function (nums) {
    this.arr = nums
};

/**
 * @return {number}
 */
ArrayWrapper.prototype.valueOf = function () {
    const result = this.arr.reduce((accumulator, num) => {
        return accumulator + num
    }, 0)
    return result
}

/**
 * @return {string}
 */
ArrayWrapper.prototype.toString = function () {
    return `[${this.arr.join(',')}]`
}

const obj1 = new ArrayWrapper([1, 2]);
const obj2 = new ArrayWrapper([3, 4]);
const res1 = obj1 + obj2; // 10
console.log("=====res1====", res1);

const res2 = String(obj1); // "[1,2]"
console.log("=====res2====", res2);

const res3 = String(obj2); // "[3,4]"
console.log("=====res3====", res3);
