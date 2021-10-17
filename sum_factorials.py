n = int(input())
sum_factorials = 0
factorial = 1
for i in range(1, n + 1):
    factorial *= i
    sum_factorials += factorial
print(sum_factorials)
