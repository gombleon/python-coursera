string = input()
i = 0
new_string = ''
while i < len(string):
    new_string = new_string + string[i] + '*'
    i += 1
print(new_string[0: -1])
