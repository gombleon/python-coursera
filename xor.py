def xor(x, y):
    return x + y == 1

x, y = int(input()), int(input())
if xor(x, y):
    print(1)
else:
    print(0)
