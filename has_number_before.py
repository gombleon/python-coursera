import sys
myList = list(map(int, input().split()))
mySet = {myList[0]}
i = 1
print('NO')
while i < len(myList):
    if myList[i] in mySet:
        print('YES')
    else:
        print('NO')
        mySet.add(myList[i])
    i += 1
