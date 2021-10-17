number = 0
count_number = 0
max_length = 0
k = 1
while k != 0:
    k = int(input())
    if k == number:
        count_number += 1
    else:
        number = k
        count_number = 1
    if max_length < count_number:
        max_length = count_number
print(max_length)
