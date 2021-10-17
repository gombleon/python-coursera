n = int(input())
list1 = list(map(int, input().split()))
x = int(input())
delta, near_element = 2001, 2001
for i in list1:
    if abs(i - x) < delta:
        delta = abs(i - x)
        near_element = i
print(near_element)
