from math import sqrt


print(
    *filter(
        lambda prime: 0 not in set(
            map(
                lambda divisor: prime % divisor,
                range(2, int(sqrt(prime)) + 1)
            )
        ),
        range(2, int(input()) + 1)
    )
)
