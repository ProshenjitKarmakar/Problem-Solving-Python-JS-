class Solution(object):
    def intersection(self, nums1, nums2):
        mapped = {}
        result = []

        for i in nums1 :
            if i in mapped :
                mapped[i] += 1
            else:
                mapped[i] = 1
        
        for j in nums2 :
            if j in mapped :
                result.append(j)
        
        return list(set(result))
    
    def intersection2(self, num1, num2) :
        set1 = set(num1)
        set2 = set(num2)
        
        return list(set1 & set2)

obj = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]

res = obj.intersection2(nums1, nums2)
print(f'Result: {res}')
