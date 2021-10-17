def isPrime(n):
    i = 2
    while n % i > 0 and i <= n ** (1/2):
        i += 1
    return i > n ** (1/2)
n = int(input())
if isPrime(n):
    print('YES')
else:
    print('NO')
