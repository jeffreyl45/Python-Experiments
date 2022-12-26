# finds the specified row of pascal's triangle recursively
def pascal(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1,1]
    prev = pascal(n-1)
    currentRow = []
    for i in range (len(prev)-1):
        currentRow += [prev[i] + prev[i+1]]
    return [1] + currentRow + [1]

# recursively finds the first row a specified number occurs in pascal's triangle
def isPascal(value, n = 3):
    if value == 1:
        return 1
    else:
        currentRow = pascal(n)
        print(currentRow)
        if value in currentRow:
            return n
        else:
            return isPascal(value, n+1)
print(isPascal(5))
