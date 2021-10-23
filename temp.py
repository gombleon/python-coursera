f = lambda x: (x + 64 / x) / 2
a = 1


def repeat(f, a):
    yield a
    for v in repeat(f, f(a)):
        yield v

for x, i in zip(repeat(f, a), range(10)):
    print(x)

