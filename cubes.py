inFile = open('input.txt', 'r', encoding='utf8')
line = inFile.readline()
[n, m] = list(map(int, line.split()))
myList = []
for number in inFile:
    myList.append(int(number))
set_Ann = myList[: n]
set_Boris = myList[n:]
set_intersect = list(set(set_Ann) & set(set_Boris))
print(len(set_intersect))
print(*sorted(set_intersect))
print(len(list(set(set_Ann) - set(set_Boris))))
print(*sorted(list(set(set_Ann) - set(set_Boris))))
print(len(list(set(set_Boris) - set(set_Ann))))
print(*sorted(list(set(set_Boris) - set(set_Ann))))
inFile.close()
