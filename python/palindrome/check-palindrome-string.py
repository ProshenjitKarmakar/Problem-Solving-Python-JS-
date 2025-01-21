# two pointer ==================================
def checkPalindromeString(str) :
    length = len(str) -1
    for i in range(0, len(str)) :
        if i <= length :
            # print(i, length)
            print(str[i], str[length])
            if str[i] == str[length] :
                check = True
                length -= 1
            else:
                check = False
                break
    return check

str = input('Enter a string:')
res = checkPalindromeString(str)
print('Palindrome : ', res)


# string reverse ================================
class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.lower()
        str = ''
        text = '0123456789abcdefghijklmnopqrstuvwxyz'
        for st in string :
            if st in text:
                str += st
        newStr = str[::-1]

        return str == newStr


obj = Solution()
tx1 = 'race a car'
tx2 = 'A man, a plan, a canal: Panama'
tx3= ' '
tx4= '0P'
res = obj.isPalindrome(tx4)
print(f'Result : {res}')