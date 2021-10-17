def height(name, myDict):
    return 0 if name not in myDict else height(myDict[name], myDict) + 1

inFile = open('input.txt', 'r', encoding='utf8')
n = int(inFile.readline())
myDict = {}
for i in range(1, n):
    ls = inFile.readline().split()
    (child, parent) = (ls[0].strip(), ls[1].strip())
    myDict[child] = parent
[print(i, height(i, myDict)) for i in
 sorted(set(myDict.keys()) | set(myDict.values()))]
inFile.close()
