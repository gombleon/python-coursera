def reverse():
    global count_n
    n = int(input())
    if n == 0:
        return
    reverse()
    if n == int(n ** (1/2)) ** 2 and n != 0:
        count_n += 1
        print(n, end=' ')

count_n = 0
reverse()
if count_n == 0:
    print(count_n)
