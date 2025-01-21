class Solution(object):
    def containsDuplicate(self, nums):
        mapped = {}
        for item in nums :
            if item in mapped:
               return True
            else :
                mapped[item] = 1
        return False


        
test = [1,2,3,4]
obj = Solution()
result  = obj.containsDuplicate(test)

print(f'result: {result}')
