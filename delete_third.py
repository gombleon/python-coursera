string = input()
new = ''
i = 0
while i < len(string):
    if i % 3 > 0:
        new = new + string[i]
    i += 1
print(new)
