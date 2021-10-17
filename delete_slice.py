string = input()
n1 = string.find('h')
reverse_string = string[:: -1]
n2 = len(string) - 1 - reverse_string.find('h')
new_string = string[0: n1] + string[n2 + 1:]
print(new_string)
