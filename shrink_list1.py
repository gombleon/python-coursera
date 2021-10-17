list1 = list(map(int, input().split()))
i = len(list1) - 1
while i >= 0:
    if list1[i] == 0:
        list1.pop(i)
        list1.append(0)
    i -= 1
print(*list1)
