const getMaxValue = (arr, length) => {
    let max = 0;
    for(let i = 0; i < length; i++) {
        if(arr[i] > max) {
            max = arr[i];
        }
    }
    return max;
}

const countingSort = (arr, length, base) => {
    let countingArr = new Array(10).fill(0);
    let newArr = new Array(length).fill(0);

    for(let i = 0; i < length; i++) {
        let index = Math.floor((arr[i]/base) % 10);
        countingArr[index] = countingArr[index] + 1;
    }
    
    for(let j = 1; j <= newArr.length; j++) {
        countingArr[j] = countingArr[j] + countingArr[j -1];
    }

    for(let k = length-1; k >= 0; k--) {
        let index = Math.floor((arr[k]/base) % 10);
        newArr[--countingArr[index]] = arr[k];
    }

    for(let l = 0; l < length; l++) {
        arr[l] = newArr[l];
    }
}

const radixSort = (arr, length) => {
    const max = getMaxValue(arr, length);
    let loop = max.toString().length;
    let base  = 1;

    while(loop > 0) {
        countingSort(arr, length, base);
        base *= 10;
        loop--;
    }
}

const array = [8, 2, 4, 71, 10, 3, 9, 6, 102];
radixSort(array, array.length);

console.log({array});