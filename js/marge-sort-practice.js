const marge = (arr, start, mid, end) => {
    let length1 = mid - start + 1;
    let length2 = end - mid;
    let leftArr = [];
    let rightArr = [];

    for(let i = 0; i < length1; i++) {
        leftArr[i] = arr[start+i];
    }
    for(let j = 0; j < length2; j++) {
        rightArr[j] = arr[mid + 1 + j];
    }

    let x = 0;
    let y = 0;
    let z = start;

    while(x < length1 && y < length2) {
        if(leftArr[x] < rightArr[y]) {
            arr[z] = leftArr[x];
            x++;
        } else {
            arr[z] = rightArr[y];
            y++;
        }
        z++;
    }

    while(x < length1) {
        arr[z] = leftArr[x];
        x++;
        z++;
    }

    while(y < length2) {
        arr[z] = rightArr[y];
        y++;
        z++;
    }
}

const margeSort = (arr, start, end) => {
    if(start < end) {
        let mid = Math.floor((start + end) / 2);
        margeSort(arr, start, mid);
        margeSort(arr, mid + 1, end);

        marge(arr, start, mid, end);
    }
}

const array = [8, 2, 4, 7, 1, 3, 9, 6, 5];
margeSort(array, 0, array.length -1);

console.log({array});