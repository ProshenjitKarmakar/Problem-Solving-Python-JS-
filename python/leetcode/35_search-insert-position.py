class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1

        while(left <= right) :
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else :
                right = mid - 1
        return len(nums)


obj = Solution ()
nums = [1,3,5,6]
target = 5

result = obj.searchInsert(nums, target)

print(f'result : {result}')