string1 = '+___'
string3 = '|__\\'
string4 = '|   '
n = int(input())
for i in range(1, n + 1):
    print(string1, sep=' ', end=' ')
print()
for i in range(1, n + 1):
    print('|{} /'.format(i), end=' ')
print()
for i in range(1, n + 1):
    print(string3, sep=' ', end=' ')
print()
for i in range(1, n + 1):
    print(string4, sep=' ', end=' ')
