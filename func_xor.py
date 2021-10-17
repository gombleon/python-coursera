print(
    *map(
        lambda a: (a[0] + a[1]) % 2,
        zip(map(int, input().split()), map(int, input().split()))
    )
)
