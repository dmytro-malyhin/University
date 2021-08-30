Vvod = input('Введите пароль')
password = 'qwerty'
count = 0
while Vvod != password:
    count += 1
    print('Не правильный пароль')
    Vvod = input('Введите пароль')
    if Vvod == password:
        print('Поздравляю!')
        print('Вы потратили', count, 'попыток')
