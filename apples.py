k = 5
a = 7
b = 11
c = 12
for i in range(k):
    a, b, c = c - b, a, 2 * a
print(a, b, c)
