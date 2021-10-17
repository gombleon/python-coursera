a = int(input())
b = int(input())
if a > b:
    a, b = b
for i in range(a, b + 1):
    x = abs(i)
    if x % 10 == x // 1000 and (x // 10) % 10 == (x // 100) % 10:
        print(i)
