from sys import stdin
import copy



from typing import List, Any


def mulMatrix(matrix1, matrix2):
    list1 = []
    for i in range(len(matrix1)):
        list2 = []
        for j in range(len(matrix2)):
            total_sum = 0
            for x, y in zip(matrix1[i], matrix2[j]):
                total_sum += x * y
            list2.append(total_sum)
        list1.append(list2)
    return list1


class MatrixError(BaseException):
    def __init__(self, Matrix, other):
        self.matrix1 = Matrix
        self.matrix2 = other


class Matrix:
    def __init__(self, matrix):
        self.matrix = copy.deepcopy(matrix)

    def size(self):
        return len(self.matrix), len(self.matrix[0])

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.matrix)

    def __add__(self, other):
        if self.size() == other.size():
            list1 = [[i + j for i, j in zip(x, y)]
                     for x, y in zip(self.matrix, other.matrix)]
            return copy.deepcopy(Matrix(list1))
        else:
            raise MatrixError(self, other)

    def __mul__(self, other):
        if (isinstance(other, Matrix) and self.size()[1] == other.size()[0]):
            mulmatrix = mulMatrix(self.matrix, other.transposed(other).matrix)
        elif isinstance(other, int) or isinstance(other, float):
            mulmatrix = [[other * i for i in x] for x in self.matrix]
        else:
            raise MatrixError(self, other)
        return Matrix(mulmatrix)

    def transpose(self):
        transMatrix = []
        for j in range(self.size()[1]):
            tempList = []
            for i in range(self.size()[0]):
                tempList.append(self.matrix[i][j])
            transMatrix.append(tempList)
        self.matrix = transMatrix
        return Matrix(transMatrix)

    @staticmethod
    def transposed(matrix):
        # noinspection SpellCheckingInspection
        transmatrix = []
        for j in range(matrix.size()[1]):
            templist = []
            for i in range(matrix.size()[0]):
                templist.append(matrix.matrix[i][j])
            transmatrix.append(templist)
        return Matrix(transmatrix)

    __rmul__ = __mul__
    __radd__ = __add__


exec(stdin.read())
