foot_size = int(input())
shoes = list(map(int, input().split()))
shoes.sort()
if shoes[-1] < foot_size:
    print(0)
else:
    max_shoes = 0
    for i in shoes:
        if foot_size <= i:
            max_shoes += 1
            foot_size = i + 3
    print(max_shoes)
