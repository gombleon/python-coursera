inFile = open('input.txt', 'r', encoding='utf8')
number_countries = int(inFile.readline())
dict_cities_countries = {}
for i in range(number_countries):
    line = inFile.readline()
    line = line.split()
    country = line[0]
    for i in range(1, len(line)):
        if line[i] not in dict_cities_countries:
            dict_cities_countries[line[i]] = []
        dict_cities_countries[line[i]] = country
number_cities = int(inFile.readline())
for i in range(number_cities):
    print(dict_cities_countries[inFile.readline().strip()])
inFile.close()
