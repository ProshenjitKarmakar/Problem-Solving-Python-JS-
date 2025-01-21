def matchTwoStringsAreAnagram(str1, str2) : 
    if len(str1) != len(str2) :
        return False
    else : 
        obj = {}
        for ch in str1:
            if ch in obj:
                obj[ch] += 1
            else:
                obj[ch] = 1
        
        for ch in str2 :
            if ch in obj :
                obj[ch] = obj[ch] -1 
                if obj[ch] == 0 :
                    del obj[ch]
            else :
                return False
        if obj == {} :
            return True
        else :
            return False
        
str1 = input("Enter a string : ")
str2 = input("Enter second string : ")

res = matchTwoStringsAreAnagram(str1, str2)
print("Anagram :", res)
