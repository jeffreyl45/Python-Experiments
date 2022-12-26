# recursively determines if a string is a palindrome
def palindrome(s):
    if len(s) == 1:
        return True
    elif s[0] == s[-1]:
        s = s[1:len(s)-1]
        return palindrome(s)
    else:
        return False

print(palindrome("step on no pets"))
print(palindrome("bluejay"))