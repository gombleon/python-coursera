inFile = open('input.txt', 'r', encoding='utf8')
myDict = {}
for words in inFile:
    words_split = words.split()
    party = ' '.join(words_split[: -1])
    if party not in myDict:
        myDict[party] = int(words_split[-1])
firstElectoralQuotient = sum(myDict.values()) / 450
dictParty = {}
dictRemaining = {}
for party in myDict:
    quotient = myDict[party] / firstElectoralQuotient
    dictParty[party] = int(quotient)
    dictRemaining[quotient - int(quotient)] = party
remainingSeats = 450 - sum(dictParty.values())
listIter = sorted(dictRemaining, reverse=True)
i = 0
while remainingSeats > 0:
    party = dictRemaining[listIter[i]]
    dictParty[party] += 1
    remainingSeats -= 1
    i += 1
for party in dictParty:
    print(party, dictParty[party])
inFile.close()
