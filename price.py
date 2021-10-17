price = float(input())
rubles = int(price)
penny = int(round(price - rubles, 2) * 100)
print(rubles, penny)
