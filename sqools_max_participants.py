inFile = open('input.txt', 'r', encoding='utf8')
sqools = [0] * 99
max_participients = 0
for line in inFile:
    sqools[int(line.split()[-2]) - 1] += 1
print(*[i + 1 for i in range(len(sqools)) if sqools[i] == max(sqools)])
inFile.close()
