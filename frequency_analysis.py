inFile = open('input.txt', 'r', encoding='utf8')
myDict = {}
for line in inFile:
    words = map(lambda s: s.strip(), line.split())
    for word in words:
        if word not in myDict:
            myDict[word] = -1
        else:
            myDict[word] -= 1
myList = sorted(myDict.items(), key=lambda s: (s[1], s[0]))
for item in myList:
    print(item[0])
inFile.close()
