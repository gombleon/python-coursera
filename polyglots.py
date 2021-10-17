inFile = open('input.txt', 'r', encoding='utf8')
(number_students, number_languages) = (int(inFile.readline()),
                                       int(inFile.readline()))
all_languages = {inFile.readline()[: -1] for i in range(number_languages)}
languages_everyone_knows = all_languages.copy()
for i in range(number_students - 1):
    number_languages = int(inFile.readline())
    temp_set = {inFile.readline()[: -1] for i in range(number_languages)}
    all_languages |= temp_set
    languages_everyone_knows &= temp_set
print(len(languages_everyone_knows))
for i in list(languages_everyone_knows):
    print(i)
print(len(all_languages))
for i in list(all_languages):
    print(i)
inFile.close()
