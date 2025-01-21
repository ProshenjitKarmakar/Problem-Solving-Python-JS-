class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        mapped = {}
        val = 0

        for i in range(0, len(nums)) :
            if(nums[i] in mapped) :
                if abs(mapped[nums[i]] - i) <= k:
                    return True
            mapped[nums[i]] = i
        return False    

obj = Solution()
nums = [1,2,3,1,2,3]
k = 2

result = obj.containsNearbyDuplicate(nums, k)
print(f'result : {result}')