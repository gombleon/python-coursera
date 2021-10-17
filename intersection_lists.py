def intersection(a, b):
    set_a = set(a)
    set_b = set(b)
    return sorted(list(set_a.intersection(set_b)))

a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*intersection(a, b))
