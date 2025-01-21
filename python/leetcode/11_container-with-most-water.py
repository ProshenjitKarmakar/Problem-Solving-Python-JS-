class Solution(object):
    def maxArea(self, height):
        max_area = 0
        n = len(height)
        left = 0
        right = n - 1

        while (left < right):
            width = right - left
            heigth = min(height[left], height[right])
            area = width * heigth
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        print(f'max_area : {max_area}')
        return max_area


obj = Solution()

array = [1,8,6,2,5,4,8,3,7]
obj.maxArea(array)  