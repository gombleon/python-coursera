list1 = list(map(int, input().split()))
max1 = max(list1)
min1 = min(list1)
if len(list1) == 2:
    print(min1, max1)
elif len(list1) == 3:
    list1.remove(max1)
    max2 = max(list1)
    if max1 * max2 > min1 * max2:
        print(max2, max1)
    else:
        print(min1, max2)
else:
    list1.remove(max1)
    max2 = max(list1)
    list1.remove(min1)
    min2 = min(list1)
    if max1 * max2 > min1 * min2:
        print(max2, max1)
    else:
        print(min1, min2)
