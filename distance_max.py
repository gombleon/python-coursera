n1 = int(input())
n2 = int(input())
k = int(input())
n3 = k
prev_max = 0
next_max = 0
if n1 < n2 and n2 > n3:
    next_max = 2
min_distance = 100000000
distance = 1000000000
count_number = 3
while k != 0:
    k = int(input())
    if k != 0:
        count_number += 1
        n1 = n2
        n2 = n3
        n3 = k
        if n1 < n2 and n2 > n3:
            prev_max = next_max
            next_max = count_number - 1
            distance = next_max - prev_max
        if min_distance > distance:
            min_distance = distance
if prev_max == 0:
    print(0)
else:
    print(min_distance)
