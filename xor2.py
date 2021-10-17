from functools import reduce


print(
    *map(
        lambda x: reduce(
            lambda a, b: int(a) ^ int(b), x),
        zip(
            *map(
                lambda x: x.split(), open('input.txt').readlines()[1:]
            )
        )
    )
)
