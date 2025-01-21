def LongestWord(sen):
    max_word = ''
    new_word = ''
    valid = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for string in sen :
        if string in valid :
            new_word += string
        elif string == ' ':
            max_word = max(max_word, new_word)
            new_word = ''

    max_word = max(max_word, new_word)
    return max_word


Input = "fun&!! time" 
print(LongestWord(Input))