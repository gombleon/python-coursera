inFile = open('input.txt', 'r', encoding='utf8')
number_string = int(inFile.readline())
dict_synonym = {}
rev_dict = {}
for i in range(number_string):
    line = inFile.readline()
    line = line.split()
    dict_synonym[line[0].strip()] = line[1].strip()
    rev_dict[line[1].strip()] = line[0].strip()
word = inFile.readline().strip()
if word in dict_synonym:
    print(dict_synonym[word])
else:
    print(rev_dict[word])
inFile.close()
