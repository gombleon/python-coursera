inFile = open('input.txt', 'r', encoding='utf8')
grade9, grade10, grade11 = [], [], []
max9, max10, max11 = 0, 0, 0
for line in inFile:
    line = line.split()
    if line[-2] == '9':
        grade9.append(int(line[-1]))
    elif line[-2] == '10':
        grade10.append(int(line[-1]))
    else:
        grade11.append(int(line[-1]))
grade9.sort(reverse=True)
i = 0
while grade9[i] == max(grade9):
    i += 1
max9 = grade9[i]
grade10.sort(reverse=True)
i = 0
while grade10[i] == max(grade10):
    i += 1
max10 = grade10[i]
grade11.sort(reverse=True)
i = 0
while grade11[i] == max(grade11):
    i += 1
max11 = grade11[i]
print(max9, max10, max11)
