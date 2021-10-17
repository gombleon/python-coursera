inFile = open('input.txt', 'r', encoding='utf8')
inFile.readline()
parties = []
for line in inFile:
    if line.strip() != 'VOTES:':
        parties.append(line.strip())
    else:
        break
votes = [line.strip() for line in inFile]
for party in parties:
    if votes.count(party) / len(votes) >= 0.07:
        print(party)
inFile.close()
