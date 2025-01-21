class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num
        return result
    
obj = Solution()

nums = [4,1,2,1,2]
result = obj.singleNumber(nums)
print(f'result : {result}')
        