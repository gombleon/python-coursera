string = input()
n1 = string.find('f')
string1 = string[:: -1]
n2 = len(string) - 1 - string1.find('f')
if n1 != -1:
    if n1 == n2:
        print(n1)
    else:
        print(n1, n2)
