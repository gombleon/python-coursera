inFile = open('input.txt', 'r', encoding='utf8')
inFile.readline()
parties = []
for line in inFile:
    if line.strip() != 'VOTES:':
        parties.append([line.strip(), 0])
    else:
        break
votes = [line.strip() for line in inFile]
for i in range(len(parties)):
    parties[i][1] = votes.count(parties[i][0])
parties.sort(key=lambda party: (-party[1], party[0]))
for party in parties:
    print(party[0])
inFile.close()
