p = int(input())
x = int(input())
y = int(input())
k = int(input())
i = 1
while i <= k:
    penny = (x * 100 + y) * (100 + p)
    roubles = penny // 100
    x = penny // 10000
    y = (penny % 10000) // 100
    i += 1
print(x, y)
