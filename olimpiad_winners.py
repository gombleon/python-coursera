inFile = open('input.txt', 'r', encoding='utf8')
score_winner_9, score_winner_10, score_winner_11 = 0, 0, 0
for line in inFile:
    line = list(line.split())
    if line[2] == '9' and int(line[3]) > score_winner_9:
        score_winner_9 = int(line[3])
    elif line[2] == '10' and int(line[3]) > score_winner_10:
        score_winner_10 = int(line[3])
    elif line[2] == '11' and int(line[3]) > score_winner_11:
        score_winner_11 = int(line[3])
print(score_winner_9, score_winner_10, score_winner_11)
inFile.close()
