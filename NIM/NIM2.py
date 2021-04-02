def nim2(stones_total):

    import nimcheck

    count = 0

    while stones_total[0] != 0 or stones_total[1] != 0:
        if (-1) ** count > 0:
            print('Ход компьютера')
            stones = abs(stones_total[0] - stones_total[1])
            if stones == 0:
                stones = 1
            if stones_total[0] >= stones_total[1]:
                stones_pile = 1
                stones_total[0] -= stones
            else:
                stones_pile = 2
                stones_total[1] -= stones
            count += 1
        else:
            print('Ваш ход')
            stones_pile = int(input('Из какой кучки будете брать камни? (1 или 2) '))
            while stones_pile != 1 and stones_pile != 2:
                stones_pile = int(input('Не понял. \nИз какой кучки будете брать камни? (1 или 2) '))
            stones = int(input('Сколько камней будете брать? '))
            if stones_pile == 1:
                while nimcheck.niminput(stones, stones_total[0]):
                    stones = int(input(
                        'Количество взятых камней должно быть положительным целым числом не больше {}. '
                        'Сколько камней будете брать? '.format(stones_total[0])
                    ))
                stones_total[0] -= stones
            else:
                while nimcheck.niminput(stones, stones_total[1]):
                    stones = int(input(
                        'Количество взятых камней должно быть положительным целым числом не больше {}. '
                        'Сколько камней будете брать? '.format(stones_total[1])
                    ))
                stones_total[1] -= stones
            count += 1
        print('Из кучки', stones_pile, 'взято камней', stones)
        print('Осталось: \nв кучке 1 -', stones_total[0], '*' * stones_total[0], '\nв кучке 2 -', stones_total[1],
              '*' * stones_total[1])
        print()

    if (-1) ** count < 0:
        return 0
    else:
        return 1
