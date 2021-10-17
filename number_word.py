inFile = open('input.txt', 'r', encoding='utf8')
dict_words = {}
for line in inFile:
    words = map(lambda s: s.strip(), line.split())
    for word in words:
        if word not in dict_words:
            dict_words[word] = 0
        print(dict_words[word], end=' ')
        dict_words[word] += 1
inFile.close()
