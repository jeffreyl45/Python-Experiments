#  converts roman numeral to decimal
def romanToDec(s):
    romans = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    decimal = 0
    for i in range(len(s)-1):
        if romans[s[i]] < romans[s[i+1]]:
            decimal -= romans[s[i]]
        else:
            decimal += romans[s[i]]
    decimal += romans[s[-1]]
    return decimal

# recursively converts roman numeral to decimal
def romanToDec2(s):
    romans = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    if len(s) ==1:
        return romans[s]
    if romans[s[0]] < romans[s[1]]:
        return romanToDec2(s[1:]) - romans[s[0]]
    else:
        return romanToDec2(s[1:]) + romans[s[0]]


print(romanToDec2("MMMCMXCIX"))

# converts decimal to roman
def decToRoman(x):
    numbers = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    roman = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
    romanNumeral = ""
    # set i = 12 since there are 12 elements in each of the numbers and roman list
    i = 12
    while x != 0:
        if numbers[i] <= x:
            romanNumeral += roman[i]
            x = x- numbers[i]
        else:
            i -= 1
    return romanNumeral
print(decToRoman(49))
print(decToRoman(1249))
print(decToRoman(4))
print(decToRoman(67))

# recursively converts decimal to roman
def decToRoman2(x, i = 12, romanNumeral = ""):
    numbers = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    roman = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
    # set i = 12 since there are 12 elements in each of the numbers and roman list
    if i == 0:
        return romanNumeral
    else:
        if numbers[i] <= x:
            return decToRoman2(x - numbers[i], i,romanNumeral +roman[i])
        else:
            return decToRoman2(x, i-1, romanNumeral)



print(decToRoman2(49))

