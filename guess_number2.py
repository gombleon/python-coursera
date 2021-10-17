inFile = open('input.txt', 'r', encoding='utf8')
numbers, beatris_question = int(inFile.readline()), inFile.readline()[: -1]
guess_numbers = set(range(1, numbers + 1))
while beatris_question != 'HELP':
    beatris_question = set(map(int, beatris_question.split()))
    beatris_set = guess_numbers & beatris_question
    other_set = guess_numbers - beatris_question
    if len(other_set) >= len(beatris_set):
        print('NO')
        guess_numbers = other_set
    else:
        print('YES')
        guess_numbers = beatris_set
    beatris_question = inFile.readline()[: -1]
print(*sorted(list(guess_numbers)))
inFile.close()
