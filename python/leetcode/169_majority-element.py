class Solution:
    def majorityElement(self, nums) -> int:
        obj ={}
        for i in range(0, len(nums)) :
            if nums[i] in obj :
                obj[nums[i]] += 1
            else :
                obj[nums[i]] = 1

        max_key = max(obj, key=obj.get)
        print(f'nums : {obj}')
        print(f'max_key : {max_key}')
        return max_key


obj = Solution()
test1 = [2,2,1,1,1,2,2]
obj.majorityElement(test1)