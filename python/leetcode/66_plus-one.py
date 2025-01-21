class Solution(object):
    def plusOne(self, digits):
        nums = ''

        for i in digits:
            nums += str(i)
        res = int(nums) + 1
        res = [int(i) for i in str(res)]
        return res
        

obj = Solution()

array = [4,3,2,1]
result = obj.plusOne(array)

print(f'result : {result}')