print('Это игра НИМ с двумя кучками камней. \nИгрок в свой ход берет любое количество камней из любой одной '
      'кучки. \nВыигрывает тот, кто возьмет последний камень')
print()
stones_total_1 = int(input('Введите количество камней в кучке 1: '))
stones_total_2 = int(input('Введите количество камней в кучке 2: '))
print()
print('Итак, у вас две кучки камней. \nВ кучке 1 -', stones_total_1, '\nВ кучке 2 -', stones_total_2)
print()
stones = 0
count = 0

while stones_total_1 != 0 or stones_total_2 != 0:
    if (-1) ** count > 0:
        print('Ход компьютера')
        stones = abs(stones_total_1 - stones_total_2)
        if stones == 0:
            stones = 1
        if stones_total_1 >= stones_total_2:
            stones_number = 1
            stones_total_1 -= stones
        else:
            stones_number = 2
            stones_total_2 -= stones
        count += 1
    else:
        print('Ваш ход')
        stones_number = int(input('Из какой кучки будете брать камни? (1 или 2) '))
        while stones_number != 1 and stones_number != 2:
            stones_number = int(input('Не понял. \nИз какой кучки будете брать камни? (1 или 2) '))
        stones = int(input('Сколько камней будете брать? '))
        if stones_number == 1:
            while stones > stones_total_1:
                print('В этой кучке нет столько камней. Есть', stones_total_1)
                stones = int(input('Сколько камней будете брать? '))
            stones_total_1 -= stones
        else:
            while stones > stones_total_2:
                print('В этой кучке нет столько камней. Есть', stones_total_2)
                stones = int(input('Сколько камней будете брать? '))
            stones_total_2 -= stones
        count += 1
    print('Из кучки', stones_number, 'взято камней', stones)
    print('Осталось: \nв кучке 1 -', stones_total_1, '\nв кучке 2 -', stones_total_2)
    print()

if (-1) ** count < 0:
    print('Вы проиграли')
else:
    print('Вы выиграли!')
