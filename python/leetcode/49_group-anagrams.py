from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs) :
        anagrams = defaultdict(list)

        for str in strs:
            indexes = [0] * 26 # for a-z

            for char in str:
                indexes[ord(char) - ord('a')] += 1 # finding index of a char ex. ord(ascii) - ord(a) // always calculating the distance from a.
            key = tuple(indexes)
            print(f'key : {key}')
            anagrams[key].append(str)

        print(f'anagrams : {anagrams}')
        return list(anagrams.values())

obj = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]

result = obj.groupAnagrams(strs)

print(f'result : {result}')