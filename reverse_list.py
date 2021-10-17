def reverse(a, i):
    if i <= len(a) - 1:
        reverse(a, i + 1)
        print(a[i], end=' ')

list1 = list(map(int, input().split()))
reverse(list1, 0)
