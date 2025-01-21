class BinarySearch :
    def __init__(self) -> None:
        self.head = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    def findElementIndex(self, searchItem) :
        left = 0
        right = len(self.head) - 1
        
        while left <= right :
            mid = (left + right) // 2
            if self.head[mid] == searchItem: 
                return mid
            elif self.head[mid] < searchItem :
               left = mid + 1
            else :
                right = mid - 1
        return -1

userInput = int(input("Enter a number : "))
search = BinarySearch()
res = search.findElementIndex(userInput)
if res != -1 :
    print(f'Item found in index {res}')
else :
    print(f'Data not found!')