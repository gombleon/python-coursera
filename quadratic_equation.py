import math
a = float(input())
b = float(input())
c = float(input())
if abs(a) < 10 ** (-9):
    if abs(b) < 10 ** (-9) and abs(c) < 10 ** (-9):
        print(3)
    elif abs(b) < 10 ** (-9) and abs(c) > 10 ** (-8):
        print(0)
    elif abs(b) > 10 ** (-8):
        print(1, -c / b)
else:
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 10 ** (-9):
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        if x1 > x2:
            x1, x2 = x2, x1
        print(2, x1, x2)
    elif abs(discriminant) < 10 ** (-10):
        print(1, -b / (2 * a))
    else:
        print(0)
