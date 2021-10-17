inFile = open('input.txt', 'r', encoding='utf8')
score_9 = 0
score_10 = 0
score_11 = 0
count_9 = 0
count_10 = 0
count_11 = 0
for line in inFile:
    [name, last_name, number_class, score] = line.split()
    if number_class == '9':
        score_9 += int(score)
        count_9 += 1
    elif number_class == '10':
        score_10 += int(score)
        count_10 += 1
    elif number_class == '11':
        score_11 += int(score)
        count_11 += 1
inFile.close()
if count_9 > 0:
    average_9 = score_9 / count_9
else:
    average_9 = 0
if count_10 > 0:
    average_10 = score_10 / count_10
else:
    average_10 = 0
if count_11 > 0:
    average_11 = score_11 / count_11
else:
    average_11 = 0
print(average_9, average_10, average_11)
