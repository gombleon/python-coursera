number = float(input())
number_int = int(number)
if number - number_int < 0.5:
    print(number_int)
else:
    print(number_int + 1)
