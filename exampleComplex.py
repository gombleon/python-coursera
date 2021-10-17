class Complex:
    def __init__(self, re, im):
        self.re = re
        self.im = im
    def __str__(self):
        strRep = str(self.re)
        if self.im > 0:
            strRep += '+'
        strRep += str(self.im)
        strRep += 'i'
        return strRep
    def __add__(self, other):
        re = self.re + other.re
        im = self.im + other.im
        return Complex(re, im)
    def __mul__(self, other):
        re = self.re * other.re - self.im * other.im
        im = self.re * other.im + self.im * other.re
        return Complex(re, im)

a = Complex(1, 1)
b = Complex(2, -3)
print(a * b)
print(str(a))
