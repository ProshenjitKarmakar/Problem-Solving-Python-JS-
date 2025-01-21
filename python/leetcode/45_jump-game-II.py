class Solution:
    def jump(self, nums) -> int:
        n = len(nums)
        max_value = 0
        jump = 0
        current = 0

        if n == 1 :
            return jump

        for i in range(n) :
            max_value = max(max_value, i + nums[i])

            if i == current :
                jump += 1
                current += max_value

                if current >= n - 1 :
                    break
        return jump

            
        
obj = Solution()

test = [2,3,1,1,4]
test = [1,2,1,1,1]
test = [0]
# test= [1,2,3]
res = obj.jump(test)

print(f'Result: {res}')