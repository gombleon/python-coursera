inFile = open('input.txt')
number = int(inFile.readline())
list_participants = []
for line in inFile:
    line = list(line.split())
    list_participants.append([int(line[1]), line[0]])
list_participants.sort(reverse=True)
for participant in list_participants:
    print(participant[1])
inFile.close()
