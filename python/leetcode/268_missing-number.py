class Solution(object):
    def missingNumber(self, nums):
        values = set(nums)
        max_num = max(nums)

        for i in range(0, max_num+1):
            if i not in values :
                return i

obj = Solution()
test = [9,6,4,2,3,5,7,0,1]
result = obj.missingNumber(test)
print(f'result : {result}')

