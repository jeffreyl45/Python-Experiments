# recursively converts an Integer to a binary string
def binary(num):
    alphabet = "01"
    if num < 2:
        return alphabet[num]
    else:
        return binary(num//2) + alphabet[num%2]

print(binary(16))

# recursively converts a binary string to an Integer
def binaryToInt(s):
    alphabet = "01"
    if len(s) == 1:
        return alphabet.index(s)
    return 2 ** (len(s)-1) * alphabet.index(s[0]) + binaryToInt(s[1:])

print(binaryToInt("10000"))