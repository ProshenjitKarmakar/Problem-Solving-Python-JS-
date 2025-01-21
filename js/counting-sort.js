const getMax = (arr, length) => {
    let max = 0;
    for(let i = 0; i < length; i++) {
        if(arr[i] > max) {
            max = arr[i];
        }
    }
    return max;
}

const countingSort = (arr, length) => {
    let max = getMax(arr, length);
    let countingArr = new Array(max + 1).fill(0);
    let newArr = new Array(length).fill(0);

    for(let i = 0; i < length; i++) {
        ++countingArr[arr[i]];
    }

    for(let j = 1; j <= max; j++) {
        countingArr[j] = countingArr[j] + countingArr[j -1];
    }

    for(let k = length -1; k >= 0; k--) {
        newArr[--countingArr[arr[k]]] = arr[k];
        
    }

    for(let l = 0; l < length; l++) {
        arr[l] = newArr[l];
    }
}

const array = [2, 2, 4, 7, 1, 3, 5, 6, 5];
countingSort(array, array.length);

console.log({array});