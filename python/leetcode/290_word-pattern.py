class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s):
            return False
        mapped = {}
        s = s.split()
        for i in range(0, len(pattern)):
            if pattern[i] in mapped :
                if mapped[pattern[i]] != s[i]:
                    return False
                else :
                    pass
            else :
                mapped[pattern[i]] = s[i]
        
        mapped ={}

        for i in range(0, len(s)):
            if s[i] in mapped :
                if mapped[s[i]] != pattern[i]:
                    return False
                else :
                    pass
            else :
                mapped[s[i]] = pattern[i]

        return True


obj = Solution()
pattern = 'aaa'
s= 'aa aa aa aa'
result  = obj.wordPattern(pattern, s)

print(f'result is : {result}')