import math
number = float(input())
number1 = number - int(number)
count = 0
while not number.is_integer():
    count += 1
    number *= 10
print(round(number1, count))
