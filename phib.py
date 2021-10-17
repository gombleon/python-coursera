def phib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return phib(n - 2) + phib(n - 1)

n = int(input())
print(phib(n))
