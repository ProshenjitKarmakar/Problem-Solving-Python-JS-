class Solution:
    def twoSum(self, numbers, target: int):
        i = 0
        j = len(numbers) - 1

        while i < j:
            result = numbers[i] + numbers[j]
            if result == target:
                return [i+1, j+1]
            elif result > target:
                j -= 1
            elif result < target:
                i += 1

obj = Solution()


numbers = [-1,0]
target= -1
res = obj.twoSum(numbers, target)

print(f'Result : {res}')
        