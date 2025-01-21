def bubbleSort(arr):
    length = len(arr)
    for i in range(0, length-1) :
        for j in range(0, length -1 - i) :
            if arr[j] > arr[j+1] :
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

array = [8, 3, 5, 6, 1, 9, 2, 7, 4]
bubbleSort(array)
print(array)