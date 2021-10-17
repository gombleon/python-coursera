n = int(input())
x = float(input())
value = 0
i = 0
while i <= n:
    number = float(input())
    value = value * x + number
    i += 1
print(value)
