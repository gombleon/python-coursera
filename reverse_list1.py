list1 = list(map(int, input().split()))
i = 0
while i < len(list1) // 2:
    list1[i], list1[len(list1) - 1 - i] = list1[len(list1) - 1 - i], list1[i]
    i += 1
print(*list1)
