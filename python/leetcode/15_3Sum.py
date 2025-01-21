class Solution:
    def threeSum(self, nums):
        length  = len(nums)
        new_array = []

        nums.sort()

        for i in range(length -2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i+1
            right = length - 1

            while left < right:
                result = nums[i] + nums[left] + nums[right]

                if result > 0 :
                    right -= 1
                elif result < 0 :
                    left += 1
                else:
                    new_array.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while  left < right and nums[right] == nums[right + 1]:   
                        right -= 1
                              
        print(f'new_array : {new_array}')
        return new_array



obj = Solution()

nums = [-1,0,1,2,-1,-4]
obj.threeSum(nums)
        