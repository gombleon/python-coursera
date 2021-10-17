a, b, c, d = int(input()), int(input()), int(input()), int(input())
e = int(input())
count_solutions = 0
for i in range(0, 1001):
    if i != e and a * i ** 3 + b * i ** 2 + c * i + d == 0:
        count_solutions += 1
print(count_solutions)
