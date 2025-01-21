class Solution(object):
    def moveZeros(self, nums):
        non_zero_index = 0

        for i in range(0, len(nums)) :
            if nums[i] != 0 :
                nums[non_zero_index] = nums[i]
                non_zero_index += 1

        for j in range(non_zero_index, len(nums)) :
            nums[j] = 0
                    
        print(f'nums : {nums}')
        return nums
                
        

obj = Solution()
test = [0]
result = obj.moveZeros(test)
print(f'result : {result}')

