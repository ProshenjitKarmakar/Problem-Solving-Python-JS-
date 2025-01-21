class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        items = dict()

        for j in range(0, len(magazine)) :
            if(magazine[j] in items) :
                items[magazine[j]] += 1
            else :
                items[magazine[j]] = 1

        print(f'items : {items}')

        for i in range(0, len(ransomNote)) :
            if ransomNote[i] in items and items[ransomNote[i]] > 0 :
                items[ransomNote[i]] -= 1
            else :
                return False
            
        return True



obj = Solution()
ransomNote = 'aa'
magazine = 'aab'
result = obj.canConstruct(ransomNote, magazine)

print(f'result : {result}')