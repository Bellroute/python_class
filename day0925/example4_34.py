number = input('Enter a hex character: ')

if ord(str(number)) > 69:
    print('Invalid input')
elif len(number) == 1:
    number = '0' + number
    print(int(number, 16))
else:
    print(number)