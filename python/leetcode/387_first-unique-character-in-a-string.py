class Solution(object):
    def firstUniqChar(self, s):
        mapped = {}

        for i in range(0, len(s)) :
            if s[i] in mapped :
                mapped[s[i]] += 1
            else :
                mapped[s[i]] = 1
        print(f'mapped : {mapped}')

        for i in range(0, len(s)) :
            if mapped[s[i]] == 1 :
                return i 
        return -1
        

obj = Solution()
test = 'loveleetcode'
result = obj.firstUniqChar(test)
print(f'result : {result}')