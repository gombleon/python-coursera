inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
myDict = {}
for candidate in inFile:
    candidate = candidate.strip()
    if candidate not in myDict:
        myDict[candidate] = 1
    else:
        myDict[candidate] += 1
myList = sorted(myDict.items(), key=lambda item: item[1], reverse=True)
if 2 * myList[0][1] > sum(myDict.values()):
    print(myList[0][0], file=outFile)
else:
    print(myList[0][0], file=outFile)
    print(myList[1][0], file=outFile)
inFile.close()
outFile.close()
