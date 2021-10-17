def power(a, n):
    if n == 0:
        return 1
    else:
        if n > 0:
            b = a
        else:
            b = 1 / a
        pow = 1
        n = abs(n)
        d = b
        while n > 0:
            if n % 2 == 0:
                n = n // 2
                d = d * d
            else:
                n -= 1
                pow = pow * d
        return pow

a = float(input())
n = int(input())
print(power(a, n))
