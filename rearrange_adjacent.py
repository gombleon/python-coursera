list1 = list(map(int, input().split()))
i = 0
while i < len(list1) - 1:
    list1[i], list1[i + 1] = list1[i + 1], list1[i]
    i += 2
print(*list1)
