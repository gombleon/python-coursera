inFile = open('input.txt', 'r', encoding='utf8')
dictElectors = {}
for line in inFile:
    line = line.split()
    candidate, number = line[0].strip(), int(line[1])
    if candidate not in dictElectors:
        dictElectors[candidate] = number
    else:
        dictElectors[candidate] += number
for candidate in sorted(dictElectors):
    print(candidate, dictElectors[candidate])
inFile.close()
