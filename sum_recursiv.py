def sum_rec():
    n = int(input())
    if n != 0:
        return sum_rec() + n
    return 0

print(sum_rec())
