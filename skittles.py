[n, k] = list(map(int, input().split()))
list1 = []
for i in range(n):
    list1.append('I')
for i in range(k):
    [l, r] = list(map(int, input().split()))
    for j in range(l - 1, r):
        list1[j] = '.'
print(''.join(list1))
