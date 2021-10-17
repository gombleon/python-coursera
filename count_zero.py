n = int(input())
count_zero = 0
for i in range(n):
    number = int(input())
    if number == 0:
        count_zero += 1
print(count_zero)
