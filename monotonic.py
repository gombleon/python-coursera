max_count = 1
number = int(input())
k = int(input())
if k > number:
    flag = 1
    count = 2
elif k < number:
    flag = 0
    count = 2
else:
    flag = 2
    count = 1
number = k
while k != 0:
    k = int(input())
    if k > number and flag == 1 and k > 0:
        count += 1
    elif k > number and flag != 1 and k > 0:
        flag = 1
        count = 2
    elif k < number and flag != 0 and k > 0:
        flag = 0
        count = 2
    elif k < number and flag == 0 and k > 0:
        count += 1
    elif k == number:
        count = 1
    number = k
    if max_count < count:
        max_count = count
print(max_count)
