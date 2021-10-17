from sys import stdin
import copy


def sumList(x, y):
    return [i + j for i, j in zip(x, y)]


def mulList(n, x):
    return [n * i for i in x]


class Matrix:
    def __init__(self, matrix):
        self.matrix = copy.deepcopy(matrix)

    def size(self):
        return len(self.matrix), len(self.matrix[0])

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.matrix)

    def __add__(self, other):
        return copy.deepcopy(
            Matrix([sumList(x, y) for x, y in zip(self.matrix, other.matrix)]))

    def __mul__(self, n):
        return copy.deepcopy(Matrix([mulList(n, x) for x in self.matrix]))

    __rmul__ = __mul__

exec(stdin.read())
