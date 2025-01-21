/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */

var flat = function (arr, n) {
    depth = n;
    new_Array = []

    for (let i = 0; i < arr.length; i++) {
        if (Array.isArray(arr[i]) && depth > 0) {
            new_Array.push()
            depth--;
        } else {

        }
    }


};