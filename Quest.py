# Как сделать первый вход, отличающийся от следующих?

# 2. Добавить возможность переиграть каждую комнату.

# 1. Добавить проверки введенных ответов.
# 1.1. Возможно, написать для этого функцию.
# 4. Добавить возможность возвращаться в предыдущие комнаты.
# 5. Добавить расстояние Ливенштейна для ответов.
# 6. Добавить разные части тела и разное развитие сюжета для саркофага.
# 7. Поиграть с шрифтами.
# 8. Добавить музыку
# 9. Повторы вынести в функции


# import random
# from typing import List


def get_choice(n):
    while True:
        a = input()
        if a not in n:
            print('Попробуйте еще раз!')
        else:
            return a


def death():
    print('Переиграть комнату: да или нет?')
    a = get_choice(['да', 'нет'])
    if a == 'да':
        return 1
    elif a == 'нет':
        return 0


def call_error_handler():
    # break
    print('Упс! Что-то сломалось...')
    death()


def south_side_room1(local_current_room):  # снаружи, перед пирамидой, room 1
    eligible_rooms = [0, 2, 4]
    if local_current_room not in eligible_rooms:
        print(
            'Как вы сюда попали?..'
        )
        call_error_handler()
    elif local_current_room == 0:
        print(
            'Вы стоите около громадной пирамиды. Хотелось бы проникнуть внутрь. Давайте обойдем ее и поищем вход. Куда '
            'пойдете: направо или налево?'
        )
    else:
        print(
            'Вы опять оказались с южной стороны пирамиды, с которой начинали обход. Хотелось бы проникнуть внутрь. '
            'Давайте еще обойдем ее и поищем вход. Куда пойдете: направо или налево?'
        )
    a = get_choice(['направо', 'налево'])
    # global current_room
    # current_room = 1
    if a == 'налево':
        return 1, 2
    elif a == 'направо':
        return 1, 4


def west_side_room2(local_current_room):  # снаружи, слева от пирамиды, room 2
    eligible_rooms = [1, 3]
    if local_current_room not in eligible_rooms:
        print(
            'Как вы сюда попали?..'
        )
        call_error_handler()
    else:
        print(
            'Вы с западной стороны пирамиды. Здесь ничего нет. Вы стоите лицом к пирамиде. Куда пойдете: направо или '
            'налево?'
        )
    a = get_choice(['направо', 'налево'])
    if a == 'налево':
        return 2, 3
    elif a == 'направо':
        return 2, 1


def north_side_room3(local_current_room):  # снаружи, сзади пирамиды, room 3
    eligible_rooms = [2, 4]
    if local_current_room not in eligible_rooms:
        print(
            'Как вы сюда попали?..'
        )
        call_error_handler()
    else:
        print(
            'Вы с северной стороны пирамиды. Здесь ничего нет. Вы стоите лицом к пирамиде. Куда пойдете: направо или '
            'налево?'
        )
    a = get_choice(['направо', 'налево'])
    if a == 'налево':
        return 3, 4
    elif a == 'направо':
        return 3, 2


def east_side_room4(local_current_room):  # снаружи, справа от пирамиды, room 4
    eligible_rooms = [2, 4, 5]
    if local_current_room not in eligible_rooms:
        print(
            'Как вы сюда попали?..'
        )
        call_error_handler()
    elif local_current_room == 5:
        print(
            'Каким-то образом вы прошли сквозь каменный завал. Если вы умеете так делать, то вам нет смысла проходить '
            'квест - вы можете в любой момент выбраться из прамиды. Но если хотите, продолжим...'
        )
    else:
        print(
            'Вы с восточной стороны пирамиды. Наконец, вы увидели вход в пирамиду! Вы стоите лицом к пирамиде. Куда вы '
            'пойдете: внутрь, направо или налево?'
        )
    a = get_choice(['направо', 'налево', 'внутрь'])
    if a == 'налево':
        return 4, 1
    elif a == 'направо':
        return 4, 3
    elif a == 'внутрь':
        return 4, 5


def light():
    print(
        'У вас с собой рюкзак. Вы припоминаете, что в нем должен быть фонарик. Что вы будете делать: пойду наощупь '
        'или поищу фонарик?'
    )
    a = get_choice(['пойду наощупь', 'поищу фонарик'])
    if a == 'пойду наощупь':
        print('Вы свалились с лестницы и сломали шею. Конец.')
        return 5, 0
    elif a == 'поищу фонарик':
        print(
            'Вы сняли рюкзак, пошарили в нем рукой и нашли фонарик. Луч света осветил все ту же лестницу, конца '
            'которой не было видно.'
        )
        return 5, 1  # подумать


def stairs_up_room5(local_current_room):  # лестница, room 5
    eligible_rooms = [4, 6]
    if local_current_room not in eligible_rooms:
        print(
            'Как вы сюда попали?..'
        )
        call_error_handler()
    elif local_current_room == 4:
        print(
            'Вниз, в темноту, ведет лестница. Вы начали по ней спускаться и вдруг услышали страшный грохот. Вход в '
            'пирамиду завалило. Вы остались в полной темноте.'
        )
        light_found = light()




    # a = input('Вы: пойду вниз или сяду и буду плакать? ')
    # while a != 'пойду вниз' and a != 'сяду и буду плакать':
    #     a = input('Нет такого действия. Вы: пойду вниз или сяду и буду плакать? ')
    # if a == 'сяду и буду плакать':
    #     ny = input('Вы умерли от голода и холода. Конец. Переиграть комнату: да или нет? ')
    #     if ny == 'нет':
    #         exit()
    #     if ny == 'да':
    #         continue
    # elif a == 'пойду вниз':
    #     break








current_room = 0  # начинаем сначала
room = 1

while True:
    # if room == 0:  # умер
    #     room
    if current_room == 1:  # снаружи, с южной стороны пирамиды (откуда начинали)
        current_room, room = south_side_room1(current_room)
    elif room == 2:  # снаружи, с западной стороны пирамиды
        current_room, room = west_side_room2(current_room)
    elif room == 3:  # снаружи, с северной стороны пирамиды
        current_room, room = north_side_room3(current_room)
    elif room == 4:  # снаружи, с восточной стороны пирамиды
        current_room, room = east_side_room4(current_room)
    elif room == 5:  # лестница
        current_room, room = stairs_room5(current_room)


# # первая дверь, НИМ1
#
# while True:  # возможность переиграть комнату
#     print()
#     print('Вы долго спускались по лестнице. И, наконец, оказались перед дверью с головой сфинкса. Глаза сфинкса '
#           'открылись и он сказал:')
#     print('- Чтобы пройти в эту дверь, ты должен выиграть у меня в игру!')
#     print('Правила такие: Мы по очереди берем камни из кучки. Можно взять от 1 до 3 камней. Выигрывает тот, кто '
#           'возьмет последний камень')
#     while True:
#         print()
#         stones_total = int(input('Можешь выбрать количество камней в кучке: '))
#         while stones_total <= 0 or stones_total % 1 != 0:
#             stones_total = int(input(
#                 'Можно вводить только целое положительное число. Сколько камне будет в кучке? '))
#         stones = 0
#         count = 0
#         while stones_total > 0:
#             if (-1) ** count > 0:
#                 print('Ход сфинкса')
#                 stones = stones_total % 4
#                 if stones == 0:
#                     stones = 1
#                 count += 1
#             else:
#                 print('Ваш ход')
#                 stones = int(input('Сколько камней ты берешь? '))
#                 while stones < 1 or stones > 3 or stones % 1 != 0:
#                     stones = int(input('Количество камней должно быть целым числом от 1 до 3 включительно. Сколько '
#                                        'камней ты берешь? '))
#                 count += 1
#             stones_total -= stones
#             print('Взяли: ', stones, '. Осталось: ', stones_total)
#         if (-1) ** count < 0:
#             b = input('Ты проиграл. Играем снова: да или нет? ')
#             if b == 'нет':
#                 ny = input('Сфинкс съел твой мозг. Конец. Переиграть комнату: да или нет? ')
#                 if ny == 'нет':
#                     exit()
#                 if ny == 'да':
#                     continue
#             elif b == 'да':
#                 print('Молодец! Упорный!')
#         else:
#             print('- Ты выиграл. Проходи.')
#             break
#     break
#
# # узкий коридор
#
# while True:  # возможность переиграть комнату
#     print()
#     print('Двери с грохотом раздвинулись - и вы вошли в узкий коридор с низким потолком. '
#           'Двери за вами моментально закрылись.')
#
#     a = input('Вы страдаете клаустрофобией: да или нет? ')
#     while a != 'да' and a != 'нет':
#         a = input('Нет такого ответа. Вы страдаете клаустрофобией: да или нет? ')
#     if a == 'да':
#         ny = input('Вы поддались панике и умерли от разрыва сердца. Конец. Переиграть комнату: да или нет? ')
#         if ny == 'нет':
#             exit()
#         if ny == 'да':
#             continue
#     elif a == 'нет':
#         break
#
# # вторая дверь, НИМ2
#
# while True:  # возможность переиграть комнату
#     print()
#     print('Пройдя еще 300 м, вы уперлись в еще одну дверь - на этот раз с головой верблюда.')
#     print('- Приветствую тебя, - сказала голова верблюда, что-то пережевывая.'
#           '\nБудем надеяться, что это не предыдущий посетитель...')
#     print('- Чтобы пройти дальше, тебе надо сыграть со мной в игру.')
#     print('Правила такие: Есть две кучки камней. Игрок в свой ход берет любое количество камней из любой одной кучки. '
#           'Выигрывает тот, кто возьмет последний камень.')
#
#     while True:
#         stones_total_1 = int(input('Сколько камней будет в первой кучке: '))
#         stones_total_2 = int(input('Сколько камней будет во второй кучке: '))
#         print()
#         print('Итак, у вас две кучки камней. \nВ первой кучке -', stones_total_1, '*' * stones_total_1,
#               '\nВо второй кучке -', stones_total_2, '*' * stones_total_2)
#         print()
#         stones = 0
#         count = 0
#         while stones_total_1 != 0 or stones_total_2 != 0:
#             if (-1) ** count > 0:
#                 print('Ход верблюда')
#                 stones = abs(stones_total_1 - stones_total_2)
#                 if stones == 0:
#                     stones = 1
#                 if stones_total_1 >= stones_total_2:
#                     stones_number = 1
#                     stones_total_1 -= stones
#                 else:
#                     stones_number = 2
#                     stones_total_2 -= stones
#                 count += 1
#             else:
#                 print('Ваш ход')
#                 stones_number = int(input('Из какой кучки будете брать камни? (1 или 2) '))
#                 while stones_number != 1 and stones_number != 2:
#                     stones_number = int(input('Не понял. \nИз какой кучки будете брать камни? (1 или 2) '))
#                 stones = int(input('Сколько камней будете брать? '))
#                 if stones_number == 1:
#                     while stones > stones_total_1:
#                         print('В этой кучке нет столько камней. Есть', stones_total_1)
#                         stones = int(input('Сколько камней будете брать? '))
#                     stones_total_1 -= stones
#                 else:
#                     while stones > stones_total_2:
#                         print('В этой кучке нет столько камней. Есть', stones_total_2)
#                         stones = int(input('Сколько камней будете брать? '))
#                     stones_total_2 -= stones
#                 count += 1
#             print('Из кучки', stones_number, 'взято камней', stones)
#             print('Осталось: \nв кучке 1 -', stones_total_1, '*' * stones_total_1, '\nв кучке 2 -', stones_total_2,
#                   '*' * stones_total_2)
#             print()
#         if (-1) ** count < 0:
#             b = input('Ты проиграл. Играем еще: да или нет?')
#             if b == 'нет':
#                 ny = input('Верблюд плюнут в тебя ядовитой слюной и ты умер. Конец. Переиграть комнату: да или нет? ')
#                 if ny == 'нет':
#                     exit()
#                 if ny == 'да':
#                     continue
#             elif b == 'да':
#                 print('Упрямый, тысяча чертей!')
#         else:
#             print('- Ты выиграл! Проходи.')
#             break
#     break
#
# # большой зал
#
# while True:  # возможность переиграть комнату
#     print(
#         'Дверь открылась и вы вошли в большой зал с высоким потолком. В зале было душно и пыльно. Здесь явно не '
#         'проветривали и не убирались тысячу лет.'
#     )
#     print(
#         'Луч фонаря высветил маленькую дверь в дальнем левом углу. Но что-то привлекло вас справа. Повернувшись туда, '
#         'вы увидели огромные красивые ворота, по-видимому, покрытые золотом.'
#     )
#     a = input('Куда вы подойдете: к двери или к воротам? ')
#
#     k = 0  # есть ли ключ
#
#     while True:
#         while a != 'к двери' and a != 'к воротам':
#             a = input('Нет такого ответа. Куда вы подойдете: к двери или к воротам? ')
#
#         if a == 'к двери':
#
#             # третья дверь, НИМ3
#
#             print('На маленькой двери нарисована маленькая мышка. Она оживает и писклявым голосом говорит:')
#             print('- Чтобы пройти в эту дверь тебе надо выиграть у меня в игру.')
#             print('Правила игры: Есть три кучки камней. Игрок в свой ход берет любое количество камней из любой одной '
#                   'кучки. Выигрывает тот, кто возьмет последний камень.')
#             print()
#             stones_total_1 = int(input('Сколько камней будет в первой кучке: '))
#             stones_total_2 = int(input('Сколько камней будет во второй кучке: '))
#             stones_total_3 = int(input('Сколько камней будет в третьей кучке: '))
#             print()
#             print('Итак, у вас три кучки камней. \nВ первой кучке -', stones_total_1, '*' * stones_total_1, '\nВо '
#                   'второй кучке -', stones_total_2, '*' * stones_total_2, '\nВ третьей кучке -', stones_total_3,
#                   '*' * stones_total_3)
#             print()
#             stones_taken = 0
#             count = 0
#             stones_number = 0
#             while stones_total_1 != 0 or stones_total_2 != 0 or stones_total_3 != 0:
#                 if (-1) ** count > 0:
#                     print('Ход мышки')
#                     if stones_total_1 * stones_total_2 * stones_total_3 == 0:
#                         stones_taken = 2 * max(stones_total_1, stones_total_2, stones_total_3) - \
#                                        (stones_total_1 + stones_total_2 + stones_total_3)
#                         if stones_taken == 0:
#                             stones_taken = 1
#                         if stones_total_1 >= stones_total_2 and stones_total_1 >= stones_total_3:
#                             stones_number = 1
#                         elif stones_total_2 >= stones_total_1 and stones_total_2 >= stones_total_3:
#                             stones_number = 2
#                         elif stones_total_3 >= stones_total_1 and stones_total_3 >= stones_total_2:
#                             stones_number = 3
#                     elif stones_total_1 == stones_total_2:
#                         stones_number = 3
#                         stones_taken = stones_total_3
#                     elif stones_total_2 == stones_total_3:
#                         stones_number = 1
#                         stones_taken = stones_total_1
#                     elif stones_total_1 == stones_total_3:
#                         stones_number = 2
#                         stones_taken = stones_total_2
#                     elif stones_total_1 - 1 != 0 and \
#                             stones_total_1 - 1 != stones_total_2 and \
#                             stones_total_1 - 1 != stones_total_3:
#                         stones_number = 1
#                         stones_taken = 1
#                     elif stones_total_2 - 1 != 0 and \
#                             stones_total_2 - 1 != stones_total_1 and \
#                             stones_total_2 - 1 != stones_total_3:
#                         stones_number = 2
#                         stones_taken = 1
#                     elif stones_total_3 - 1 != 0 and \
#                             stones_total_3 - 1 != stones_total_2 and \
#                             stones_total_3 - 1 != stones_total_1:
#                         stones_number = 3
#                         stones_taken = 1
#                     else:
#                         stones_number = 1
#                         stones_taken = 1
#                     if stones_number == 1:
#                         stones_total_1 -= stones_taken
#                     elif stones_number == 2:
#                         stones_total_2 -= stones_taken
#                     elif stones_number == 3:
#                         stones_total_3 -= stones_taken
#                     count += 1
#                 else:
#                     print('Ваш ход')
#                     stones_number = int(input('Из какой кучки будете брать камни? (1, 2 или 3) '))
#                     while stones_number != 1 and stones_number != 2 and stones_number != 3:
#                         stones_number = int(input('Не понял. \nИз какой кучки будете брать камни? (1, 2 или 3) '))
#                     while (stones_number == 1 and stones_total_1 == 0) or \
#                             (stones_number == 2 and stones_total_2 == 0) or \
#                             (stones_number == 3 and stones_total_3 == 0):
#                         stones_number = int(input('В этой кучке нет камней. Выберите другую: '))
#                     stones_taken = int(input('Сколько камней будете брать? '))
#                     if stones_number == 1:
#                         while stones_taken > stones_total_1:
#                             print('В этой кучке нет столько камней. Есть', stones_total_1)
#                             stones_taken = int(input('Сколько камней будете брать? '))
#                         stones_total_1 -= stones_taken
#                     elif stones_number == 2:
#                         while stones_taken > stones_total_2:
#                             print('В этой кучке нет столько камней. Есть', stones_total_2)
#                             stones_taken = int(input('Сколько камней будете брать? '))
#                         stones_total_2 -= stones_taken
#                     else:
#                         while stones_taken > stones_total_3:
#                             print('В этой кучке нет столько камней. Есть', stones_total_3)
#                             stones_taken = int(input('Сколько камней будете брать? '))
#                         stones_total_3 -= stones_taken
#                     count += 1
#                 print('Из кучки', stones_number, 'взято камней', stones_taken)
#                 print('Осталось: \nв первой кучке -', stones_total_1, '*' * stones_total_1, '\nво второй кучке -',
#                       stones_total_2, '*' * stones_total_2, '\nв третьей кучке -', stones_total_3, '*' * stones_total_3)
#                 print()
#             if (-1) ** count < 0:
#                 b = input('Мышь выиграла. Играем еще: да или нет? ')
#                 if b == 'нет':
#                     ny = input('Глаза мыши налились кровью и стрельнули в вас лазером. Вы умерли. Конец. Переиграть '
#                                'комнату: да или нет?')
#                     if ny == 'нет':
#                         exit()
#                     if ny == 'да':
#                         continue
#                 elif b == 'да':
#                     print('Упертый, карамба!')
#             else:
#                 print('- Ты выиграл! Проходи.')
#
#                 # кладовая с кувшинами, Быки и коровы
#
#                 while True:
#                     print(
#                         'В маленькой комнате стоят сто пронумерованных кувшинов. Надо не больше чем за 7 попыток '
#                         'отгадать, в каком кувшине спрятан ключ. Вы называете номер кувшина, а мышь говорит подсказку.'
#                     )
#                     v = random.randint(1, 100)
#                     i = 0
#                     while i < 7:
#                         w = input('В каком кувшине лежит ключ? (0-100) ')
#                         while '1' <= w <= '100':
#                             w = input('Я не понимаю. В каком кувшине лежит ключ? (0-100) ')
#                         w = int(w)
#                         i += 1
#                         if w == v:
#                             print('Ты угадал! Ключ твой.')
#                             break
#                         elif w < v:
#                             print('Номер кувшина больше')
#                         elif w > v:
#                             print('Номер кувшина меньше')
#                     else:
#                         print('Все попытки потрачены. Начинаем сначала.')
#                         continue
#                     break
#
#         if a == 'к воротам':
#             print('Вы попробовали толкнуть огромные золотые ворота, но они не поддались ни на миллиметр. Вы '
#                   'осматриваете их и видите маленькую замочную скважину.')
#             if k == 0:
#                 print('Ключа у вас нет. Надо бы его поискать...')
#             elif k == 1:
#                 print('Вы достаете ключ и вставляете его в замочную скважину. Он моментально становится горячим и вы '
#                       'отдергиваете руку. Ключ сам поворачивается - и ворота начинают медленно открываться.')
#                 break
#
# # комната с саркофагом
#
# while True:  # возможность переиграть комнату
#     print('Вы входите. Ворота сзади бесшумно захлопываются. Почти все небольшое помещение занимает золотой саркофаг.')
#     c = input('Саркофаг выполнен в виде тела человека. В ногах его лежит золотая кошка. Что вы сделаете?')
#
#     cat = ['погладить кошку', 'поглажу кошку', 'кошку погладить', 'кошку поглажу']
#
#     if c not in cat:
#         ny = input(
#             'Вы услышали тихое посвистывание и очень захотели спать. Вы опускаетесь на пол и засыпаете навсегда. '
#             'Конец. Переиграть комнату: да или нет?')
#         if ny == 'нет':
#             exit()
#         if ny == 'да':
#             continue
#     else:
#         print('Вам показалось, что спина кошки немного выгнулась под вашей рукой и даже послышалось тихое мурчание. Но '
#               'вдруг ваше внимание привлек громкий щелчок справа. Вы повернулись туда и увидели, что часть стены '
#               'превратилась в дверь.')
#
#     a = input('Что вы сделаете: пойду в дверь или останусь на месте? ')
#
#     while a != 'пойду в дверь' or a != 'останетесь на месте':
#         a = input('Непонятно. Что вы сделаете: пойду в дверь или останусь на месте? ')
#
#     if a == 'останусь на месте':
#         ny = input('Кошка выгнулась и укусила вас. Вы умерли от смертельного яда. Конец. Переиграть комнату: да или '
#                    'нет? ')
#         if ny == 'нет':
#             exit()
#         if ny == 'да':
#             continue
#     elif a == 'пойдете в дверь':
#         break
#
# # сокровищница
#
# while True:  # возможность переиграть комнату
#     print()
#     print('Вы оказались в самой настоящей сокровищнице. На стене горит факел. Он освещает ларец с монетами, золотые '
#           'доспехи, статуи с глазами из драгоценных камней, мебель из ценных пород дерева и золотой ёршик рядом с '
#           'золотым унитазом...')
#
#     a = input(
#         'Что вы сделаете: возьму факел, наберу монеты в карман, надену золотые доспехи, выковырну глаза у статуй, '
#         'полежу на кровати, возьму ёршик?'
#     )
#
#     final = ['возьму факел', 'наберу монеты в карман', 'надену золотые доспехи', 'выковырну глаза у статуй',
#              'полежу на кровати', 'возьму ёршик', 'возьму ершик']
#
#     while a not in final:
#         a = input('Нет такого ответа. Что вы сделаете: возьму факел, наберу монеты в карман, надену золотые доспехи, '
#                   'выковырну глаза у статуй, полежу на кровати, возьму ёршик?')
#
#     if a == 'наберу монеты в карман':
#         ny = input('Как только вы прикоснулись к монетам, вы сами превратились в золотую статую с глазами из '
#                    'драгоценных камней. Конец. Переиграть комнату: да или нет? ')
#         if ny == 'нет':
#             exit()
#         if ny == 'да':
#             continue
#     elif a == 'надену золотые доспехи':
#         ny = input('Доспехи оказались очень тяжелыми. Они вас раздавили. Конец. Переиграть комнату: да или нет? ')
#         if ny == 'нет':
#             exit()
#         if ny == 'да':
#             continue
#     elif a == 'выковырну глаза у статуй':
#         ny = input(
#             'Как только вы начали это делать, статуя обрушила на вас свою тяжелую руку и вы умерли на месте. Конец. '
#             'Переиграть комнату: да или нет? '
#         )
#         if ny == 'нет':
#             exit()
#         if ny == 'да':
#             continue
#     elif a == 'полежу на кровати':
#         ny = input(
#             'Как только вы легли, из угла поднялся золотой медведь и съел вас. Конец. Переиграть комнату: да или нет? '
#         )
#         if ny == 'нет':
#             exit()
#         if ny == 'да':
#             continue
#     elif a == 'возьму факел':
#         print(
#             'Вы потянули за факел, но он не вынулся из гнезда, а послышался скрежет цепи, заработал какой-то механизм, '
#             'спрятанный внутри стен. Потолок начал постепенно опускаться, но одновременно с этим начала подниматься от '
#             'пола одна из стен.'
#         )
#         b = input('Что вы сделаете: нырну под стену или останусь в сокровищнице?')
#         while b != 'нырну под стену' and b != 'останусь в сокровищнице':
#             b = input('Непонятно. Что вы сделаете: нырну под стену или останусь в сокровищнице?')
#         if b == 'нырну под стену':
#             print('Поздравляю! Вы оказались на свободе! Правда, посреди пустыни и теперь вам нужно как-то добраться до '
#                   'людей или хотя бы до воды. Но это уже совсем другая история...')
#             exit()
#         elif b == 'останусь в сокровищнице':
#             ny = input('Вас раздавил потолок. Конец. Переиграть комнату: да или нет? ')
#             if ny == 'нет':
#                 exit()
#             if ny == 'да':
#                 continue
#     elif a == 'возьму ёршик' or a == 'возьму ершик':
#         b = input('Что вы с ним сделаете: использую по назначению или потрясу в воздухе?')
#         while b != 'использую по назначению' and b != 'потрясу в воздухе':
#             b = input('Непонятно. Что вы с ним сделаете: использую по назначению или потрясу в воздухе?')
#         if b == 'использую по назначению':
#             ny = input(
#                 'Из золотого унитаза вползла золотая змея, ужалила вас и вы умерли от яда. Конец. Переиграть комнату: '
#                 'да или нет? '
#             )
#             if ny == 'нет':
#                 exit()
#             if ny == 'да':
#                 continue
#         elif b == 'потрясу в воздухе':
#             d = 1
#             while d != 3:
#                 e = input('Ничего не произошло. Что вы сделаете: потрясу еще раз или положу на место? ')
#                 if e == 'положу на место':
#                     ny = input(
#                         'Из золотого унитаза вползла золотая змея, ужалила вас и вы умерли от яда. Конец. Переиграть '
#                         'комнату: да или нет? '
#                     )
#                     if ny == 'нет':
#                         exit()
#                     if ny == 'да':
#                         continue
#                 elif e == 'потрясу еще раз':
#                     d += 1
#             print('Вдалеке послышался вой сирены. Люди в масках пробили стену, погрузили вас в автозак и увезли в '
#                   'неизвестном направлении. Ну по крайней мере вы выбрались из гробницы. Поздравляю!')
