n = int(input())
total = n * (n + 1) // 2
for i in range(1, n):
    x = int(input())
    total -= x
loss_card = total
print(loss_card)
