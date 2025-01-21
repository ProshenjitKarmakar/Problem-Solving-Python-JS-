class Solution:
    def canJump(self, nums) -> bool:
        max_reachable = 0

        for i in range(len(nums)):
            print(f'I : {i}')
            if i > max_reachable:
                return False
            else :
                print(f'max_reachable : {nums[i]}')
                max_reachable = max(max_reachable, i + nums[i])
                print(f'max_reachable : {max_reachable}')
            
            if max_reachable >= len(nums) - 1:
                return True
        return False    


obj = Solution()

test1 = [2,3,1,1,4]
# test1 = [3,2,1,0,4]
# test1 = [0]
# test1 = [0,1]
# test1 = [2,0]

res = obj.canJump(test1)

print(f'result : {res}')