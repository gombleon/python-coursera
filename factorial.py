from itertools import accumulate
import operator


print(
    *accumulate(
        [1] + list(range(1, int(input()) + 1)), operator.mul
    )
)
