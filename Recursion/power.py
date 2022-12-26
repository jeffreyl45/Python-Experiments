# recursively implements the power of an integer
def power(a,b):
    if b == 0:
        return 1
    if b == 1:
        return a
    if a == 0:
        return 0
    if b < 0:
            return 1/(power(a, -b))
    if b > 0:
        return a* power(a,b-1)

print(power(3,(-2)))

