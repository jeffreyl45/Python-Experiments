# recursively converts an Integer to a hexadecimal string
def hexa(num):
    alphabet = "0123456789ABCDE"
    if num < 16:
        return alphabet[num]
    else:
        return hexa(num//16) + alphabet[num%16]
print(hexa(64))

# recursively converts a hexadecimal string to an Integer
def hexaToInt(s):
    alphabet = "0123456789ABCDE"
    if len(s) == 1:
        return alphabet.index(s)
    return 16 ** (len(s)-1) * alphabet.index(s[0]) + hexaToInt(s[1:])
print(hexaToInt("A"))