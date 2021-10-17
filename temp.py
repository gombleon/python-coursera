a = list(map(int, input().split()))
j = 0
for i in range(len(a)):
    if a[i] != 0 and a[j] == 0:
        a[i], a[j] = a[j], a[i]
        j += 1
print(*a)