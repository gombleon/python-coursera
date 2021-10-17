from functools import reduce


abc = zip(range(4), range(4))
print(*map(lambda x: reduce(lambda a, b: str(a) + str(b), x), abc), sep='\n')
