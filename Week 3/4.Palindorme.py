def is_palindrome(s):

  temp = s
  if (temp == s[::-1]):
    return True
  else:
    return False


print(is_palindrome("madam"))
