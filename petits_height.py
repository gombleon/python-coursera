list1 = list(map(int, input().split()))
x = int(input())
i = 0
while i < len(list1) and list1[i] >= x:
    i += 1
print(i + 1)
