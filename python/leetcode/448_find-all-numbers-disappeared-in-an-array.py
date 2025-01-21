class Solution(object):
    def findDisappearedNumbers(self, nums):
        mapped = {}

        for i in range(1, len(nums) + 1) :
            mapped[i] = i

        for num in nums :
            del mapped[num]


        print(f'mapped: {mapped}')
        
        return list(mapped.keys())

        


obj = Solution()
nums = [1,1]
res = obj.findDisappearedNumbers(nums)
print(f'res: {res}')
