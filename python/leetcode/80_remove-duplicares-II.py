class Solution:
    def removeDuplicates(self, nums) -> int:
        obj = {}
        count = 0
        
        for i in range(0, len(nums)) :
            if nums[i] in obj :
                if obj[nums[i]] > 1 :
                    nums[i] = '_'
                else :
                    obj[nums[i]] += 1
                    count += 1
            else :
                obj[nums[i]] = 1
                count += 1

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

        print(f"x {count}")
        print(f"nums {nums}")


obj = Solution()
test1 = [0,0,1,1,1,1,2,3,3]
# test1 = [1,1,1,2,2,3]
test1 = [0, 1]
obj.removeDuplicates(test1)
