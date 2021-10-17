def minDivisor(n):
    i = 2
    while n % i > 0 and i <= n ** (1/2):
        i += 1
    if i * i > n:
        return n
    return i
n = int(input())
print(minDivisor(n))
