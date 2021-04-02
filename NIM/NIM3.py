def nim3(stones_total):

    import nimcheck

    count = 0

    # TODO: подумать, как можно использовать NIM2, если в одной из куч 0 камней

    while stones_total[0] != 0 or stones_total[1] != 0 or stones_total[2] != 0:
        if (-1) ** count > 0:
            print('Ход компьютера')
            if stones_total[0] * stones_total[1] * stones_total[2] == 0:
                stones_taken = 2 * max(stones_total[0], stones_total[1], stones_total[2]) - \
                        (stones_total[0] + stones_total[1] + stones_total[2])
                if stones_taken == 0:
                    stones_taken = 1
                if stones_total[0] == max(stones_total[0], stones_total[1], stones_total[2]):
                    stones_pile = 1
                elif stones_total[1] == max(stones_total[0], stones_total[1], stones_total[2]):
                    stones_pile = 2
                elif stones_total[2] == max(stones_total[0], stones_total[1], stones_total[2]):
                    stones_pile = 3
            elif stones_total[0] == stones_total[1]:
                stones_pile = 3
                stones_taken = stones_total[2]
            elif stones_total[1] == stones_total[2]:
                stones_pile = 1
                stones_taken = stones_total[0]
            elif stones_total[0] == stones_total[2]:
                stones_pile = 2
                stones_taken = stones_total[1]
            elif stones_total[0] - 1 != 0 and \
                    stones_total[0] - 1 != stones_total[1] and \
                    stones_total[0] - 1 != stones_total[2]:
                stones_pile = 1
                stones_taken = 1
            elif stones_total[1] - 1 != 0 and \
                    stones_total[1] - 1 != stones_total[0] and \
                    stones_total[1] - 1 != stones_total[2]:
                stones_pile = 2
                stones_taken = 1
            elif stones_total[2] - 1 != 0 and \
                    stones_total[2] - 1 != stones_total[1] and \
                    stones_total[2] - 1 != stones_total[0]:
                stones_pile = 3
                stones_taken = 1
            else:
                stones_pile = 1
                stones_taken = 1
            if stones_pile == 1:
                stones_total[0] -= stones_taken
            elif stones_pile == 2:
                stones_total[1] -= stones_taken
            elif stones_pile == 3:
                stones_total[2] -= stones_taken
            count += 1
        else:
            print('Ваш ход')
            stones_pile = int(input('Из какой кучки будете брать камни? (1, 2 или 3) '))
            while stones_pile != 1 and stones_pile != 2 and stones_pile != 3:
                stones_pile = int(input('Не понял. \nИз какой кучки будете брать камни? (1, 2 или 3) '))
            while (stones_pile == 1 and stones_total[0] == 0) or \
                    (stones_pile == 2 and stones_total[1] == 0) or \
                    (stones_pile == 3 and stones_total[2] == 0):
                stones_pile = int(input('В этой кучке нет камней. Выберите другую: '))
            stones_taken = int(input('Сколько камней будете брать? '))
            while nimcheck.niminput(stones_taken, stones_total[stones_pile - 1]):
                stones_taken = int(input('В этой кучке нет столько камней. Есть {} камней. '
                                         'Сколько камней будете брать? '.format(stones_total[stones_pile - 1])))
            stones_total[stones_pile - 1] -= stones_taken
            count += 1
        print('Из кучки', stones_pile, 'взято камней', stones_taken)
        print('Осталось: \nв кучке 1 -', stones_total[0], '*' * stones_total[0], '\nв кучке 2 -', stones_total[1],
              '*' * stones_total[1], '\nв кучке 3 -', stones_total[2], '*' * stones_total[2])
        print()

    if (-1) ** count < 0:
        return 0
    else:
        return 1
