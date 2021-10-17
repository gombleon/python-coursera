inFile = open('input.txt', 'r', encoding='utf8')
distance = list(map(int, inFile.readline().split()))
rate = list(map(int, inFile.readline().split()))
distance.sort(reverse=True)
rate.sort()
payment_travel = 0
for i in range(len(rate)):
    payment_travel += rate[i] * distance[i]
print(payment_travel)
inFile.close()
