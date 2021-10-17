inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
list_total = []
for line in inFile:
    line = line.split()
    list_total.append(line[0] + ' ' + line[1] + ' ' + line[3])
list_total.sort()
for i in list_total:
    print(i, file=outFile)
inFile.close()
outFile.close()
