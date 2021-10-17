list1 = list(map(int, input().split()))
tup = tuple(set(list1))
max_frec = tup[0]
frec = 1
for i in tup:
    if list1.count(i) > frec:
        frec = list1.count(i)
        max_frec = i
print(max_frec)
