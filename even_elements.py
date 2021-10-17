list1 = input().split()
print(*[i for i in list1 if int(i) % 2 == 0])
