string = input()
n1 = string.find('f')
n2 = string.find('f', n1 + 1)
if n1 == -1:
    print(-2)
elif n2 == -1:
    print(-1)
else:
    print(n2)
