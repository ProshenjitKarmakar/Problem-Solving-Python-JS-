class Solution(object):
    def longestConsecutive(self, nums):
            longest_sequence = 0
            mapped = set(nums)

            for num in nums :
                if num-1 not in mapped :
                    length = 0
                    start = num

                    while start in mapped:
                        length += 1
                        start += 1
                    longest_sequence = max(longest_sequence, length)

            print(f'longest_sequence : {longest_sequence}')
            return longest_sequence


obj = Solution()

test = [0,3,7,2,5,8,4,6,0,1]
test = [0,0]
result = obj.longestConsecutive(test)

print(f'result is : {result}')