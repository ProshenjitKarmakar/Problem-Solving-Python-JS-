class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k %= n  # Handle cases where k >= n

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # Step 1: Reverse the entire array
        reverse(0, n - 1)
        
        # Step 2: Reverse the first k elements
        reverse(0, k - 1)
        
        # Step 3: Reverse the rest of the array
        reverse(k, n - 1)

        print(f'After rotation: {nums}')

obj = Solution() 
# test1 = [1,2,3,4,5,6,7]
test1 = [-1,-100,3,99]

obj.rotate(test1, 1002)