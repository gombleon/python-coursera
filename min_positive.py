list1 = list(map(int, input().split()))
min_positive = 1000
for i in list1:
    if i > 0 and i < min_positive:
        min_positive = i
print(min_positive)
