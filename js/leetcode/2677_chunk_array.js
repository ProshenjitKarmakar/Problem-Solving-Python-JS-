/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function (arr, size) {
    chank_size = size
    new_array = []
    chank_array = []

    for (let i = 0; i < arr.length; i++) {
        if (chank_size === 0) {
            chank_size = size
            new_array.push(chank_array)
            chank_array = []
        }
        chank_array.push(arr[i])
        chank_size--;
    }
    if (chank_array.length > 0) {
        new_array.push(chank_array)
    }

    console.log("=======new_array=====", new_array);
    return new_array
};

chunk([], 1)
