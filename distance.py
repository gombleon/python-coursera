def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1/2)


def perimetr(x1, y1, x2, y2, x3, y3):
    sum_dist = (distance(x1, y1, x2, y2) + distance(x2, y2, x3, y3) +
                distance(x1, y1, x3, y3))
    return sum_dist

x1, y1 = float(input()), float(input())
x2, y2 = float(input()), float(input())
x3, y3 = float(input()), float(input())
print(perimetr(x1, y1, x2, y2, x3, y3))
