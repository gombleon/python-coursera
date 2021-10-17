list1 = list(map(int, input().split()))
min_odd = max(list1)
for i in list1:
    if i % 2 > 0 and i < min_odd:
        min_odd = i
print(min_odd)
