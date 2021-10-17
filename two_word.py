string = input()
space = string.find(' ')
word_1 = string[0: space]
word_2 = string[space + 1:]
print(word_2 + ' ' + word_1)
