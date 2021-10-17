import sys
inFile = sys.stdin.readlines()
myList = []
for line in inFile:
    line = line.split()
    for i in line:
        myList.append(i)
print(len(set(myList)))
inFile.close()
