class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
            if len(s) != len(t) :
                  return False
            map = {}

            for i in range(0, len(s)) :
                if s[i] in map :
                    if map[s[i]] != t[i] :
                        return False
                    else :
                        map[s[i]] = t[i]
                else :
                    map[s[i]] = t[i]

            map = {}

            for i in range(0, len(t)) :
                if t[i] in map :
                    if map[t[i]] != s[i] :
                        return False
                    else :
                        map[t[i]] = s[i]
                else :
                    map[t[i]] = s[i]
            print(f"map : {map}")
            return True 

obj= Solution()
s = 'badc'
t = 'baba'
result = obj.isIsomorphic(s, t)
print(f"result : {result}")