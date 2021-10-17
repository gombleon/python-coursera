def numberStress(word):
    numberUpper = 0
    correct = False
    for i in range(len(word)):
        if word[i].isupper():
            numberUpper += 1
    if numberUpper == 1:
        correct = True
    return correct

inFile = open('input.txt', 'r', encoding='utf8')
numberWords = int(inFile.readline())
numberErrors = 0
vocabulary = {}
for i in range(numberWords):
    line = inFile.readline().strip()
    if line.lower() not in vocabulary:
        vocabulary[line.lower()] = [line]
    else:
        vocabulary[line.lower()].append(line)
for line in inFile:
    words = list(map(lambda word: word.strip(), line.split()))
    for word in words:
        if (not numberStress(word) or numberStress(word) and
                word.lower() in vocabulary and
                word not in vocabulary[word.lower()]):
            numberErrors += 1
print(numberErrors)
inFile.close()
