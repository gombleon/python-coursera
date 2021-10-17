inFile = open('input.txt', 'r', encoding='utf8')
dictWords = {}
for line in inFile:
    words = map(lambda w: w.strip(), line.split())
    for word in words:
        if word not in dictWords:
            dictWords[word] = -1
        else:
            dictWords[word] -= 1
revTuple = sorted(dictWords.items(), key=lambda item: (item[1], item[0]))
print(revTuple[0][0])
inFile.close()
