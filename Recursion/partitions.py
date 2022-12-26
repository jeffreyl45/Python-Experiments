# recursively determines the number of ways a number(n) can be made using numbers from 1-m
def partition(n,m):
    if n == 0:
        return 1
    elif m == 0 or n < 0:
        return 0
    if m == 1:
        return 1
    else:
        return partition(n-m,m) + partition(n, m-1)
print(partition(5,3))