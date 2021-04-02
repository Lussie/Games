def nim1(stones_total):

    import nimcheck  # модуль проверки корректности ввода

    count = 0

    while stones_total[0] > 0:
        if (-1) ** count > 0:
            print('Ход компьютера')
            stones = stones_total[0] % 4
            if stones == 0:
                stones = 1
            count += 1
        else:
            print('Ваш ход')
            stones = int(input('Сколько камней будете брать? '))
            while nimcheck.niminput(stones, min(stones_total[0], 3)):
                stones = int(input(
                    'Количество взятых камней должно быть положительным целым числом не больше {}. '
                    'Сколько камней будете брать? '.format(min(stones_total[0], 3))
                ))
            count += 1
        stones_total[0] -= stones
        print('Из кучки взято камней', stones)
        print('Осталось в кучке -', stones_total[0], '*' * stones_total[0])
        print()

    if (-1) ** count < 0:
        return 0
    else:
        return 1
