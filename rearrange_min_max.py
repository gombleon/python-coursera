list1 = list(map(int, input().split()))
min_index, max_index = 0, 0
min_el, max_el = list1[0], list1[0]
for i in range(1, len(list1)):
    if min_el > list1[i]:
        min_el = list1[i]
        min_index = i
    if max_el < list1[i]:
        max_el = list1[i]
        max_index = i
list1[min_index], list1[max_index] = list1[max_index], list1[min_index]
print(*list1)
