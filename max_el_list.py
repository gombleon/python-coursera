list1 = list(map(int, input().split()))
max_ind, max_el = 0, list1[0]
for i in range(1, len(list1)):
    if max_el <= list1[i]:
        max_el, max_ind = list1[i], i
print(max_el, max_ind)

