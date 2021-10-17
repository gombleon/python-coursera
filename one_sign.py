list1 = list(map(int, input().split()))
i = 1
while i < len(list1) and list1[i - 1] * list1[i] < 0:
    i += 1
if i < len(list1):
    print(list1[i - 1], list1[i])
