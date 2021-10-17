list1 = list(map(int, input().split()))
len_list1 = len(list1)
max1 = max(list1)
min1 = min(list1)
list1.remove(max1)
max2 = max(list1)
if len_list1 == 3:
    print(min1, max2, max1)
elif len_list1 == 4:
    list1.remove(min1)
    min2 = min(list1)
    if max1 <= 0 or min1 >= 0:
        print(min2, max2, max1)
    elif max2 <= 0 or min2 <= 0 and max2 >= 0:
        print(min1, min2, max1)
    else:
        print(min2, max2, max1)
elif len_list1 == 5:
    list1.remove(min1)
    min2 = min(list1)
    list1.remove(max2)
    max3 = max(list1)
    if max1 <= 0:
        print(max3, max2, max1)
    elif max1 >= 0 and max2 <= 0:
        print(min2, min1, max1)
    elif max2 >= 0 and max3 <= 0:
        print(min1, min2, max1)
    elif min2 <= 0 and max3 >= 0:
        if max3 * max2 * max1 > min1 * min2 * max1:
            print(max3, max2, max1)
        else:
            print(min1, min2, max1)
    elif min1 <= 0 and min2 >= 0 or min1 >= 0:
        print(max3, max2, max1)
elif len_list1 > 5:
    list1.remove(min1)
    min2 = min(list1)
    list1.remove(max2)
    max3 = max(list1)
    list1.remove(min2)
    min3 = min(list1)
    if max1 <= 0 or min1 >= 0 or min1 <= 0 and min2 >= 0:
        print(max3, max2, max1)
    elif (max1 >= 0 and max2 <= 0 or max2 >= 0 and max3 <= 0 or
          min2 <= 0 and min3 >= 0 or min3 <= 0 and max3 >= 0):
        if max3 * max2 * max1 < min1 * min2 * max1:
            print(min1, min2, max1)
        else:
            print(max3, max2, max1)
