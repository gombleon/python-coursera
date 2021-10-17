list1 = list(map(int, input().split()))
max_el, max_ind = list1[0], 0
i = 1
while i < len(list1):
    if max_el < list1[i]:
        max_el = list1[i]
        max_ind = i
    i += 1
print(max_el, max_ind)
