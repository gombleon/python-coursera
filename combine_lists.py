def merge(a, b):
    len_c = len(a) + len(b)
    c = []
    i_a = 0
    i_b = 0
    for i in range(len_c):
        if i_a < len(a) and i_b < len(b):
            if a[i_a] < b[i_b]:
                c.append(a[i_a])
                i_a += 1
            else:
                c.append(b[i_b])
                i_b += 1
        elif i_a < len(a) and i_b == len(b):
            c.append(a[i_a])
            i_a += 1
        elif i_a == len(a) and i_b < len(b):
            c.append(b[i_b])
            i_b += 1
    return c

a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*merge(a, b))
