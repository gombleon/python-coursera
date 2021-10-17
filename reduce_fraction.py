def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)


def ReduceFraction(a, b):
    nod = gcd(a, b)
    return a // nod, b // nod

a = int(input())
b = int(input())
print(*ReduceFraction(a, b))
