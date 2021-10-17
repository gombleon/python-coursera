list1 = list(map(int, input().split()))
k, c = tuple(map(int, input().split()))
i = len(list1) - 1
list1.append(list1[len(list1) - 1])
while i >= k + 1:
    list1[i] = list1[i - 1]
    i -= 1
list1[k] = c
print(*list1)
