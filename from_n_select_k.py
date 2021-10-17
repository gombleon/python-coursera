def from_n_sel_k(n, k):
    if k == 1:
        return n
    elif k == n or k == 0:
        return 1
    return from_n_sel_k(n - 1, k) + from_n_sel_k(n - 1, k - 1)

n = int(input())
k = int(input())
print(from_n_sel_k(n, k))
