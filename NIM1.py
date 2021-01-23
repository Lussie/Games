print('Это игра НИМ с одной кучкой камней. \nИгрок в свой ход берет из кучки от 1 до 3 камней. \nВыигрывает тот, '
      'кто возьмет последний камень')
print()
stones_total = int(input('Введите количество камней в кучке: '))
print()
print('Итак, камней у вас в кучке -', stones_total, '*' * stones_total)
print()
stones = 0
count = 0

while stones_total > 0:
    if (-1) ** count > 0:
        print('Ход компьютера')
        stones = stones_total % 4
        if stones == 0:
            stones = 1
        count += 1
    else:
        print('Ваш ход')
        stones = int(input('Сколько камней будете брать? '))
        while stones < 1 or stones > 3:
            stones = int(input('Количество взятых камней должно быть от 1 до 3. Сколько камней будете брать? '))
        count += 1
    stones_total -= stones
    print('Из кучки взято камней', stones)
    print('Осталось в кучке -', stones_total, '*' * stones_total)
    print()

if (-1) ** count < 0:
    print('Вы проиграли')
else:
    print('Вы выиграли!')
