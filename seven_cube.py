def seven(n, a):
    b = int((n - a ** 3) ** (1 / 3))
    c = int((n - a ** 3 - b ** 3) ** (1 / 3))
    d = int((n - a ** 3 - b ** 3 - c ** 3) ** (1 / 3))
    e = int((n - a ** 3 - b ** 3 - c ** 3 - d ** 3) ** (1 / 3))
    f = int((n - a ** 3 - b ** 3 - c ** 3 - d ** 3 - e ** 3) ** (1 / 3))
    g = int((n - a ** 3 - b ** 3 - c ** 3 - d ** 3 - e ** 3 - f ** 3) **
            (1 / 3))
    if n == a ** 3:
        print(a ** 3)
    elif n == a ** 3 + b ** 3:
        print(a ** 3, b ** 3)
    elif n == a ** 3 + b ** 3 + c ** 3:
        print(a ** 3, b ** 3, c ** 3)
    elif n == a ** 3 + b ** 3 + c ** 3 + d ** 3:
        print(a ** 3, b ** 3, c ** 3, d ** 3)
    elif n == a ** 3 + b ** 3 + c ** 3 + d ** 3 + e ** 3:
        print(a ** 3, b ** 3, c ** 3, d ** 3, e ** 3)
    elif n == a ** 3 + b ** 3 + c ** 3 + d ** 3 + e ** 3 + f ** 3:
        print(a ** 3, b ** 3, c ** 3, d ** 3, e ** 3, f ** 3)
    elif n == a ** 3 + b ** 3 + c ** 3 + d ** 3 + e ** 3 + f ** 3 + g ** 3:
        print(a ** 3, b ** 3, c ** 3, d ** 3, e ** 3, f ** 3, g ** 3)
    else:
        if a > 0:
            seven(n, a - 1)
        else:
            print(0)

n = int(input())
seven(n, int(n ** (1/3)))
