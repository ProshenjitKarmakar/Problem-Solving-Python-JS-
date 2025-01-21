class Solution :

    def marge(self, arr, left, mid, right) :
        n1 = mid - left + 1
        n2 = right - mid

        arrleft = [0] * n1
        arrright = [0] * n2

        for i in range(0, n1) :
            arrleft[i] = arr[left+i]
            i += 1
        for j in range(0, n2) :
            arrright[j] = arr[mid + j + 1]
            j+= 1

        x = 0
        y = 0
        z = left
        

        while(x < n1 and y < n2) :
            if arrleft[x] <= arrright[y] :
                arr[z] = arrleft[x]
                x += 1
            else : 
                arr[z] = arrright[y]
                y += 1
            z += 1

        while x < n1 :
            arr[z] = arrleft[x]
            x += 1
            z += 1

        while y < n2 :
            arr[z] = arrright[y]
            y += 1
            z += 1

        print(f'arr : {arr}')

    def margeSort(self, arr, left, right, type) :
        
        if left < right :
            mid = (left + right) // 2

            # print(f'left : {left}')
            # print(f'mid : {mid}')
            # print(f'right : {right}')
            # print(f'type : {type}')
            # print(f'==============')

            self.margeSort(arr, left, mid, 'first')
            self.margeSort(arr, mid + 1, right, 'second')

            self.marge(arr, left, mid, right)

    def mergeTwoArrays(self, nums1, m: int, nums2, n: int):
        x = m - 1
        y = n - 1
        z = (m+n) - 1
        
        while x >= 0 and y >= 0:
            if nums1[x] >= nums2[y]:
                nums1[z] = nums1[x]
                x -= 1
            else:
                nums1[z] = nums2[y]
                y -= 1
            z -= 1

        while x >= 0:
            nums1[z] = nums1[x]
            x -= 1
            z -= 1

        while y >= 0:
            nums1[z] = nums2[y]
            y -= 1
            z -= 1

        print(f'arr : {nums1}')

    def mergeTwoLists(self, list1, list2) :
        pass



    

obj = Solution() 

test1 = [1,2,3,0,0,0]
test2 = [2,5,6]
m1 = 3
n1 = 3

test1 = [1]
test2 = []
m1 = 1
n1 = 0

test1 = [0]
test2 = [1]
m1 = 0
n1 = 1
# obj.margeSort(test1, 0, len(test1) - 1, 'start')
# obj.mergeTwoArrays(test1, m1, test2, n1)
list1 = []
list2 = []


obj.mergeTwoLists(list1, list2)



