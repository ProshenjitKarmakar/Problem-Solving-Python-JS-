class Solution:
    def removeElement(self, nums, val: int) -> int:
        count = 0
        for i in range(0, len(nums)):
            if nums[i] == val :
                nums[i] = '_'
            else :
                count += 1

        i= 0
        j = len(nums) - 1

        while i < j:
            if nums[i] == '_':
                if nums[j] != '_':
                    nums[i], nums[j] = nums[j], nums[i]
                    j -= 1
                else:
                    j -= 1
            else:
                i += 1

        print(f"count2 : {count}")
        print(f"nums2 : {nums}")
        
        return count
        


obj = Solution() 

test1 = [0,1,2,2,3,0,4,2]
val = 2

test1 = [3,2,2,3]
val = 3

test1 = [0,1,2,2,3,0,4,2]
val = 2
res = obj.removeElement(test1, val)

print(f'Result : {res}')