def CodelandUsernameValidation(strParam):
  valid = 'abcdefghijklmnopqrstuvwxyz01234567_'

  if strParam[len(strParam) -1] == '_' :
    return False

  for string in strParam :
    if string not in valid :
      return False
  return True

test = "aa_"
result = CodelandUsernameValidation(test)

print(f'result : {result}')