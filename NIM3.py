print('Это игра НИМ с тремя кучками камней. \nИгрок в свой ход берет любое количество камней из любой одной '
      'кучки. \nВыигрывает тот, кто возьмет последний камень.')
print()
stones_total_1 = int(input('Введите количество камней в кучке 1: '))
stones_total_2 = int(input('Введите количество камней в кучке 2: '))
stones_total_3 = int(input('Введите количество камней в кучке 3: '))
print()
print('Итак, у вас три кучки камней. \nВ кучке 1 -', stones_total_1, '*' * stones_total_1, '\nВ кучке 2 -',
      stones_total_2, '*' * stones_total_2,  '\nВ кучке 3 -', stones_total_3, '*' * stones_total_3)
print()
stones_taken = 0
count = 0
stones_number = 0

while stones_total_1 != 0 or stones_total_2 != 0 or stones_total_3 != 0:
    if (-1) ** count > 0:
        print('Ход компьютера')
        if stones_total_1 * stones_total_2 * stones_total_3 == 0:
            stones_taken = 2 * max(stones_total_1, stones_total_2, stones_total_3) - \
                    (stones_total_1 + stones_total_2 + stones_total_3)
            if stones_taken == 0:
                stones_taken = 1
            if stones_total_1 >= stones_total_2 and stones_total_1 >= stones_total_3:
                stones_number = 1
            elif stones_total_2 >= stones_total_1 and stones_total_2 >= stones_total_3:
                stones_number = 2
            elif stones_total_3 >= stones_total_1 and stones_total_3 >= stones_total_2:
                stones_number = 3
        elif stones_total_1 == stones_total_2:
            stones_number = 3
            stones_taken = stones_total_3
        elif stones_total_2 == stones_total_3:
            stones_number = 1
            stones_taken = stones_total_1
        elif stones_total_1 == stones_total_3:
            stones_number = 2
            stones_taken = stones_total_2
        elif stones_total_1 - 1 != 0 and \
                stones_total_1 - 1 != stones_total_2 and \
                stones_total_1 - 1 != stones_total_3:
            stones_number = 1
            stones_taken = 1
        elif stones_total_2 - 1 != 0 and \
                stones_total_2 - 1 != stones_total_1 and \
                stones_total_2 - 1 != stones_total_3:
            stones_number = 2
            stones_taken = 1
        elif stones_total_3 - 1 != 0 and \
                stones_total_3 - 1 != stones_total_2 and \
                stones_total_3 - 1 != stones_total_1:
            stones_number = 3
            stones_taken = 1
        else:
            stones_number = 1
            stones_taken = 1
        if stones_number == 1:
            stones_total_1 -= stones_taken
        elif stones_number == 2:
            stones_total_2 -= stones_taken
        elif stones_number == 3:
            stones_total_3 -= stones_taken
        count += 1
    else:
        print('Ваш ход')
        stones_number = int(input('Из какой кучки будете брать камни? (1, 2 или 3) '))
        while stones_number != 1 and stones_number != 2 and stones_number != 3:
            stones_number = int(input('Не понял. \nИз какой кучки будете брать камни? (1, 2 или 3) '))
        while (stones_number == 1 and stones_total_1 == 0) or \
                (stones_number == 2 and stones_total_2 == 0) or \
                (stones_number == 3 and stones_total_3 == 0):
            stones_number = int(input('В этой кучке нет камней. Выберите другую: '))
        stones_taken = int(input('Сколько камней будете брать? '))
        if stones_number == 1:
            while stones_taken > stones_total_1:
                print('В этой кучке нет столько камней. Есть', stones_total_1)
                stones_taken = int(input('Сколько камней будете брать? '))
            stones_total_1 -= stones_taken
        elif stones_number == 2:
            while stones_taken > stones_total_2:
                print('В этой кучке нет столько камней. Есть', stones_total_2)
                stones_taken = int(input('Сколько камней будете брать? '))
            stones_total_2 -= stones_taken
        else:
            while stones_taken > stones_total_3:
                print('В этой кучке нет столько камней. Есть', stones_total_3)
                stones_taken = int(input('Сколько камней будете брать? '))
            stones_total_3 -= stones_taken
        count += 1
    print('Из кучки', stones_number, 'взято камней', stones_taken)
    print('Осталось: \nв кучке 1 -', stones_total_1, '*' * stones_total_1, '\nв кучке 2 -', stones_total_2,
          '*' * stones_total_2, '\nв кучке 3 -', stones_total_3, '*' * stones_total_3)
    print()

if (-1) ** count < 0:
    print('Вы проиграли')
else:
    print('Вы выиграли!')
