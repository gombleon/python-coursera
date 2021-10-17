def funcDeposit(name, amountMoney):
    if name not in dictAccounts:
        dictAccounts[name] = amountMoney
    else:
        dictAccounts[name] += amountMoney


def funcIncome(interest):
    for name in dictAccounts:
        if dictAccounts[name] > 0:
            dictAccounts[name] += dictAccounts[name] * interest // 100


def funcBalance(name):
    if name in dictAccounts:
        print(dictAccounts[name])
    else:
        print('ERROR')


def funcTransfer(fromWhom, toWhom, amountMoney):
    if fromWhom not in dictAccounts:
        dictAccounts[fromWhom] = 0
    dictAccounts[fromWhom] -= amountMoney
    if toWhom not in dictAccounts:
        dictAccounts[toWhom] = amountMoney
    else:
        dictAccounts[toWhom] += amountMoney


def funcWithdraw(name, amountMoney):
    if name not in dictAccounts:
        dictAccounts[name] = 0
    dictAccounts[name] -= amountMoney


inFile = open('input.txt', 'r', encoding='utf8')
dictAccounts = {}
for line in inFile:
    line = list(map(lambda item: item.strip(), line.split()))
    if line[0] == 'DEPOSIT':
        funcDeposit(line[1], int(line[2]))
    elif line[0] == 'INCOME':
        funcIncome(int(line[1]))
    elif line[0] == 'BALANCE':
        funcBalance(line[1])
    elif line[0] == 'TRANSFER':
        funcTransfer(line[1], line[2], int(line[3]))
    elif line[0] == 'WITHDRAW':
        funcWithdraw(line[1], int(line[2]))
inFile.close()
