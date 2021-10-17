list1 = list(map(int, input().split()))
if 0 in list1:
    i1 = list1.index(0)
    i = i1
    len_list = len(list1)
    while i < len_list:
        while i < len_list and list1[i] == 0:
            i += 1
        if i < len_list and list1[i] != 0:
            list1[i1], list1[i] = list1[i], list1[i1]
            i1 = list1.index(0)
            i += 1
print(*list1)
