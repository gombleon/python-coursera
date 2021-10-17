n = int(input())
stop = 10 ** (n - 1) - 1
start = 10 ** n - 1
for i in range(start, stop, -2):
    print(i, end=' ')
