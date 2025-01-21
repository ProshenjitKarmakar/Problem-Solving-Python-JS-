/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
function sortBy(arr, fn) {
    return arr.sort((a, b) => fn(a) - fn(b));
}

fn = (x) => x
const arr = [5, 4, 1, 2, 3]
let new_array = sortBy(arr, fn)

console.log("======new_array=====", new_array);


