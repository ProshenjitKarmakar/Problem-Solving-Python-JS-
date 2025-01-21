class Solution(object):
    def searchRange(self, nums, target):
        def find_left(): 
            left, right = 0, len(nums) - 1

            while(left <= right) :
                mid = (left + right) // 2

                if nums[mid] < target :
                    left = mid + 1
                else :
                    right = mid - 1

            return left
        
        def find_right():
            left, right = 0, len(nums) - 1

            while(left <= right) :
                mid = (left + right) // 2

                if nums[mid] <= target :
                    left = mid + 1
                else :
                    right = mid - 1

            return right
        
        left = find_left()
        right = find_right()

        if left <= right:
            return [left, right]
        else :
            return [-1,-1]

    def searchRange2(self, nums, target):
        def find_left():
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def find_right():
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right
        
        left = find_left()
        right = find_right()
        
        if left <= right:
            return [left, right]
        else:
            return [-1, -1]

    

obj = Solution()

nums = [5,7,7,8,8,10]
target = 6
result = obj.searchRange(nums, target)

print(f'result : {result}')