inFile = open('input.txt', 'r', encoding='utf8')
number_place = int(inFile.readline())
total_score = []
for line in inFile:
    line = list(line.split())
    if int(line[-1]) >= 40 and int(line[-2]) >= 40 and int(line[-3]) >= 40:
        total_score.append(int(line[-1]) + int(line[-2]) + int(line[-3]))
total_score.sort(reverse=True)
if len(total_score) <= number_place or number_place == 0:
    print(0)
elif len(total_score) > number_place:
    if total_score.count(max(total_score)) > number_place:
        print(1)
    else:
        if total_score[number_place - 1] == total_score[number_place]:
            ind_1 = total_score.index(total_score[number_place - 1])
            print(total_score[ind_1 - 1])
        else:
            print(total_score[number_place - 1])
inFile.close()
