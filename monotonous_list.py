def isAscending(a):
    i = 1
    while i < len(a) and a[i - 1] < a[i]:
        i += 1
    if i == len(a):
        return 'YES'
    return 'NO'

list1 = list(map(int, input().split()))
print(isAscending(list1))
