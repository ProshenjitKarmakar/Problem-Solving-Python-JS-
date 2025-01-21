def linearSearch(arr, searchItem) :
    for i in range(0, len(arr)) :
        if arr[i] == searchItem :
            return i
    return -1

item = int(input("Item to search : "))
array = [8, 2, 5, 9, 7, 3, 1, 6, 4]
result = linearSearch(array, item)

if result == -1 :
    print("Item not found in the list!")
else :
    print(f"Item found in the index {result}")
