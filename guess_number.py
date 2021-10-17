max_n_August = int(input())
total_set = set(map(str, range(1, max_n_August + 1)))
line = input()
while line != 'HELP':
    yes_or_no = input()
    if yes_or_no == 'YES':
        total_set &= set(line.split())
    else:
        total_set -= set(line.split())
    line = input()
print(*sorted(list(total_set)))
