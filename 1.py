def palindrom(digit):
    if digit == digit[::-1]:
        return 'Палиндром'
    else:
        return 'Не палиндром'


digit = input('Введите пятизначное число: ')
if digit[0] == '-':
    digit = digit[1:]
if digit.isdigit():
    if len(digit) == 5:
        print(palindrom(digit))
    else:
        print('Введено не пятизначное число')
else:
    print('Введено не число') 