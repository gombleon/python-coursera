list1 = list(map(int, input().split()))
various_elements = 1
for i in range(len(list1) - 1):
    if list1[i] < list1[i + 1]:
        various_elements += 1
print(various_elements)
