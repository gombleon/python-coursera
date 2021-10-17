def lagr(n, a):
    b = int((n - a ** 2) ** (1/2))
    c = int((n - a ** 2 - b ** 2) ** (1 / 2))
    d = int((n - a ** 2 - b ** 2 - c ** 2) ** (1/2))
    if a ** 2 == n:
        print(a)
    elif a ** 2 + b ** 2 == n:
        print(a, b)
    elif a ** 2 + b ** 2 + c ** 2 == n:
        print(a, b, c)
    elif a ** 2 + b ** 2 + c ** 2 + d ** 2 == n:
        print(a, b, c, d)
    else:
        if a > 1:
            lagr(n, a - 1)

n = int(input())
lagr(n, int(n ** (1/2)))
