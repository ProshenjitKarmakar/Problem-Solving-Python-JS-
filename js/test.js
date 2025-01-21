const marge = (arr, left, mid, right) => {
    let n1 = mid - left + 1
    let n2 = right - mid
    let leftArr = []
    let rightArr = []

    for(let i = 0; i < n1; i++) {
        leftArr[i] = arr[left+i]
    }

    for(let j = 0; j < n2; j++) {
        rightArr[j] = arr[mid+1+j]
    }

    let x = 0
    let y = 0
    let z = left

    while(x < n1 && y < n2) {
        if(leftArr[x] <= rightArr[y]) {
            arr[z] = leftArr[x]
            x++
        } else {
            arr[z] = rightArr[y]
            y++
        }
        z++
    }

    while(x < n1) {
        arr[z] = leftArr[x]
        x++;
        z++
    }

    while(y < n2) {
        arr[z] = rightArr[y]
        y++;
        z++;
    }
}


const  margeSort = (arr, left, right) => {
    if(left < right) {
        const mid = Math.floor((left + right) / 2)

        margeSort(arr, left, mid)
        margeSort(arr, mid + 1, right)

        marge(arr, left, mid, right)
    }
}

let array = [8, 2, 4, 7, 1, 3, 9, 6, 5];

margeSort(array, 0, array.length -1)

console.log({array})