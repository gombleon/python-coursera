n = int(input())
if n <= 10 ** 5:
    a = list(map(int, input().split()))
    if len(a) == n and abs(max(a)) <= 10 ** 9:
        a.sort()
        print(*a)
