def power(a, n):
    if n == 0:
        return 1
    elif n == 1:
        return a
    elif n > 1:
        return a * power(a, n - 1)
    return power(a, n + 1) / a

a = float(input())
n = int(input())
if a > 0:
    print(power(a, n))
