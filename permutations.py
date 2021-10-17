from itertools import permutations
from functools import reduce


print(
    *map(
        lambda x: reduce(
            lambda a, b: str(a) + str(b), x
        ),
        permutations(
            range(1, int(input()) + 1)
                    )
    ),
    sep='\n'
)
