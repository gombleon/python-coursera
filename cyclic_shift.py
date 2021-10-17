list1 = list(map(int, input().split()))
t = list1.pop()
list1.insert(0, t)
print(*list1)
