class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        findLength = len(needle)

        for i in range(0, len(haystack)):
            value = haystack[i:findLength + i]
            if(value == needle) :
                return i
        return -1
obj = Solution()

res = obj.strStr("leetcode", "leeto")

print(f'found in index {res}')