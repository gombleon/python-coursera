list1 = list(map(int, input().split()))
i = 1
count_numbers = 0
while i < len(list1) - 1:
    if list1[i] > list1[i - 1] and list1[i] > list1[i + 1]:
        count_numbers += 1
    i += 1
print(count_numbers)
