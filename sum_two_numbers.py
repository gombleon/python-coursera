number1 = int(input('Input number1'))
number2 = int(input('Input number1'))
if (number1 >= -32000 and number1 <= 32000 and
    number2 >= -32000 and number1 <= 32000):
    sumNumber1Number2 = number1 + number2
    print('Sum =', sumNumber1Number2)
else:
    print('Repeat the input')
