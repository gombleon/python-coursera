string = input()
n1 = string.find('h') + 1
reverse_string = string[:: -1]
n2 = len(string) - 1 - reverse_string.find('h')
middle_string = string[n1: n2] * 2
new_string = string[0: n1] + middle_string + string[n2:]
print(new_string)
