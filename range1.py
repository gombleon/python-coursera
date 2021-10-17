a = int(input())
b = int(input())
start = a
if a < b:
    stop = b + 1
    step = 1
else:
    stop = b - 1
    step = -1
for i in range(start, stop, step):
    print(i, end=' ')
