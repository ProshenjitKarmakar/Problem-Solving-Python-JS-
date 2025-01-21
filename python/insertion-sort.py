
def insertionSort(arr, length) :
    for i in range(1, length) :
        current = arr[i]
        j = i -1
        while j >= 0 and arr[j] > current :
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = current

array = [8, 5, 3, 9, 6, 1, 7, 2, 4]
insertionSort(array, len(array))
print(array)