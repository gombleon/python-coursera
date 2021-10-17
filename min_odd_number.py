print(
    min(
        filter(
            lambda x: (x & 1) == 1, map(int, input().split())
        )
    )
)
