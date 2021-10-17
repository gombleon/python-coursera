def isPointInArea(x, y):
    condition1 = (y + x >= 0 and y - 2 * x >= 2 and
                  (x + 1) ** 2 + (y - 1) ** 2 <= 4 and y > 0)
    condition2 = (y + x <= 0 and y - 2 * x <= 2 and y < 0 and
                  (x + 1) ** 2 + (y - 1) ** 2 >= 4)
    return condition1 or condition2

x, y = float(input()), float(input())
if isPointInArea(x, y):
    print('YES')
else:
    print('NO')
