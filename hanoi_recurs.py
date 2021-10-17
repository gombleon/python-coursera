def move(n, x, y):
    if n == 1:
        print(n, x, y)
    else:
        z = 6 - x - y
        move(n - 1, x, z)
        print(n, x, y)
        move(n - 1, z, y)

n = int(input())
move(n, 1, 3)
