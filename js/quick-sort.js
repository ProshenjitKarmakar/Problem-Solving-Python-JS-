
const findPivot = (arr, start, end) => {
    let pivot = arr[end];
    let item = start -1;
    for(let i = start; i < end; i++) {
        if(arr[i] < pivot) {
            item++;
            let temp = arr[i];
            arr[i] = arr[item];
            arr[item] = temp;
        }
    }
    item++;
    let temp = arr[item];
    arr[item] = pivot;
    arr[end] = temp;

    return item;
}

const quickSort = (arr, first, end) => {
    if(end <= first) return;
    let pIndex = findPivot(arr, first, end);
    quickSort(arr, first, pIndex -1);
    quickSort(arr, pIndex + 1, end);
}

const array = [8, 2, 4, 7, 1, 3, 9, 6, 5];
quickSort(array, 0, array.length -1);

console.log({array});







