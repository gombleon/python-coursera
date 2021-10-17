def queen_beats(a, b):
    return (a[0] == b[0] or a[1] == b[1] or a[0] + a[1] == b[0] + b[1] or
            a[0] - a[1] == b[0] - b[1])

list1 = []
for i in range(8):
    list2 = list(map(int, input().split()))
    list1.append(list2)
beats = False
i = 0
while i < 7 and not beats:
    j = i + 1
    while j < 8 and not beats:
        beats = queen_beats(list1[i], list1[j])
        j += 1
    i += 1
if beats:
    print('YES')
else:
    print('NO')
