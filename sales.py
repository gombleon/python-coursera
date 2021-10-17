inFile = open('input.txt', 'r', encoding='utf8')
buyers = {}
for line in inFile:
    line = line.split()
    if line[0] not in buyers:
        buyers[line[0]] = [(line[1], int(line[2]))]
    else:
        x = line[1]
        buyers[line[0]].append((line[1], int(line[2])))
for buyer in sorted(buyers):
    print(buyer, ':', sep='')
    dictTemp = {}
    for i in buyers[buyer]:
        if i[0] not in dictTemp:
            dictTemp[i[0]] = i[1]
        else:
            dictTemp[i[0]] += i[1]
    for i in sorted(dictTemp):
        print(i, dictTemp[i])
inFile.close()
