var filter = function (arr, fn) {
    let filteredArr = []

    for (let i = 0; i < arr.length; i++) {
        if (fn(arr[i], i)) {
            filteredArr.push(arr[i]);
        }
    }

    return filteredArr
};

function greaterThan10(n) {
    return n > 10;
}

function firstIndex(n, i) {
    return i === 0;
}

function plusOne(n) {
    return n + 1
}