list1 = list(map(int, input().split()))
k = int(input())
while k < len(list1) - 1:
    list1[k] = list1[k + 1]
    k += 1
list1.pop()
print(*list1)
