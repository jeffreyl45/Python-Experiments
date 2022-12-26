# recursively determines if a string follows the IBSN10 format
def checkISBN10(s):
    alphabet = "0123456789X"
    if len(s) == 0:
        return 0
    elif len(s) == 10:
        return (alphabet.index(s[0]) * (11 - len(s)) + checkISBN10(s[1:])) % 11 == 0
    elif len(s) < 10:
        return (alphabet.index(s[0]) * (11 - len(s)) + checkISBN10(s[1:]))

print(checkISBN10('X111111101'))
print(checkISBN10("0262529629"))

# recursively determines if a string follows the ISBN13 format
def checkIBSN13(s):
    if len(s) == 0:
        return 0
    elif len(s) == 13:
        return (int(s[0]) + checkIBSN13(s[1:])) % 10 == 0
    elif len(s) % 2 == 1:
        return (int(s[0]) + checkIBSN13(s[1:]))
    elif len(s) % 2 == 0:
        return (int(s[0]) * 3 + checkIBSN13(s[1:]))