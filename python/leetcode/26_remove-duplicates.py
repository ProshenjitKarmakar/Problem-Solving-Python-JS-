class Solution:
    def removeDuplicates(self, nums) -> int:
        arr = []
        for i in range(0, len(nums)) :
            if nums[i] in arr :
                nums[i] = '_'
            else :
                arr.append(nums[i])
        
        x = 0
        y = 1
        
        while y < len(nums) :
            if nums[x] == '_' :
                
                if nums[y] != '_' :
                    nums[x], nums[y] = nums[y], nums[x]
                    x += 1
                    y += 1
                else :
                    y += 1
            else :
                x += 1
                y += 1
            print(nums)
        # return len(arr)
        print(f'Array : {nums} - {len(arr)}')

obj = Solution()
test1 = [1,1,2]
test1 = [0,1,2,2,3,0,4,2]
obj.removeDuplicates(test1)