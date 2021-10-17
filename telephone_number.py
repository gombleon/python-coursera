inFile = open('input.txt')
phone_number = (inFile.readline().replace('(', '').replace(')', '').
                replace('-', '').replace('+7', '8')).strip()
if len(phone_number) == 7:
    phone_number = '8495' + phone_number
for number in inFile:
    phone_number1 = (number.replace('(', '').replace(')', '').
                     replace('-', '').replace('+7', '8')).strip()
    if len(phone_number1) == 7:
        phone_number1 = '8495' + phone_number1
    if phone_number1 == phone_number:
        print('YES')
    else:
        print('NO')
inFile.close()
