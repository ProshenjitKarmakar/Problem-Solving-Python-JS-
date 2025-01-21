class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapped = {}

        for str1 in s :
            if(str1 in mapped) :
                mapped[str1] += 1
            else :
                mapped[str1] = 1

        print(f'mapped 1 : {mapped}')

        for str2 in t :
            if(str2 in mapped) :
                if(mapped[str2] == 1) :
                    del mapped[str2]
                else :
                    mapped[str2] -= 1
            else :
                return False
        print(f'mapped 2 : {mapped}')
        
        if mapped == {} :
            return True
        else :
            return False



obj = Solution()

s= 'anagram'
t= 'nagaram'
result = obj.isAnagram(s, t)

print(f'Result: {result}')