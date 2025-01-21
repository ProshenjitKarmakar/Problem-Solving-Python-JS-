const marge = (arr, left, mid, right) => {
    let n1 = mid - left + 1;
    let n2 = right - mid;
    let arrLeft = [];
    let arrRight = [];

    for (let i = 0; i < n1; i++) {
        arrLeft[i] = arr[left + i];
    }
    for (let j = 0; j < n2; j++) {
        arrRight[j] = arr[mid + 1 + j];
    }

    let x = 0;
    let y = 0;
    let z = left;

    while (x < n1 && y < n2) {
        if (arrLeft[x] <= arrRight[y]) {
            arr[z] = arrLeft[x];
            x++;
        } else {
            arr[z] = arrRight[y];
            y++;
        }
        z++;
    }

    while (x < n1) {
        arr[z] = arrLeft[x];
        x++;
        z++;
    }
    while (y < n2) {
        arr[z] = arrRight[y];
        y++;
        z++;
    }
}

const margeSort = (arr, left, right, type) => {
    if (left < right) {
        let mid = Math.floor((left + right) / 2);

        margeSort(arr, left, mid, 'first');
        margeSort(arr, mid + 1, right, 'second');

        marge(arr, left, mid, right);
    }
}

let array = [8, 2, 4, 7, 1, 3, 9, 6, 5];
margeSort(array, 0, array.length - 1, 'start');

console.log({ array });