import math
list_int = []
x = int(input())
while x != 0:
    list_int.append(x)
    x = int(input())
mean_list = sum(list_int) / len(list_int)
sum_square = 0
for i in range(len(list_int)):
    sum_square += (list_int[i] - mean_list) ** 2
std_deviation = math.sqrt(sum_square / (len(list_int) - 1))
print(std_deviation)
