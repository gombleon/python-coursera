from itertools import permutations


def compon(lst):
    return {str(lst[i]) + str(lst[i + 1]) for i in range(len(lst) - 1)}

def genSet(n):
    myList = []
    for i in range(1, n + 1):
        myString = myFile.readline()
        myList.append({myString[0] + myString[2], myString[4] + myString[6]})
    return myList

def inSet(p, lst):
    res = True
    for i in lst:
        res &= len(i & p) == 1
    return res


myFile = open('input.txt', 'r', encoding='utf8')
k, n = list(map(int, myFile.readline().split()))
perm = list(permutations(range(1, k + 1), k))
lst = genSet(n)
for p in perm:
    setP = compon(p)
    if inSet(setP, lst):
        print(*p)
        break
else:
    print(0)
myFile.close()
