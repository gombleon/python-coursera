inFile = open('input.txt', 'r', encoding='utf8')
grade_9 = []
grade_10 = []
grade_11 = []
for line in inFile:
    line = list(line.split())
    if line[2] == '9':
        grade_9.append(int(line[3]))
    elif line[2] == '10':
        grade_10.append(int(line[3]))
    elif line[2] == '11':
        grade_11.append(int(line[3]))
print(grade_9.count(max(grade_9)), grade_10.count(max(grade_10)),
      grade_11.count(max(grade_11)))
