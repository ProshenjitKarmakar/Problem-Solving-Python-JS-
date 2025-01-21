
def selectionSort(arr, length) :
    for i in range(0, length - 1) :
        min = i
        for j in range(i + 1, length) :
            if arr[j] < arr[min] :
                min = j
        
        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp

array = [8, 5, 3, 9, 6, 1, 7, 2, 4]
selectionSort(array, len(array))
print(array)