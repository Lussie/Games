import nimcheck  # модуль проверки корректности ввода

# TODO: обработать пустой ввод

print('Это игра НИМ с одной кучкой камней. \nИгрок в свой ход берет из кучки от 1 до 3 камней. \nВыигрывает тот, '
      'кто возьмет последний камень')
print()
stones_total = int(input('Введите количество камней в кучке: '))
while nimcheck.niminput(stones_total, stones_total):
    stones_total = int(input(
        'Можно вводить только целое положительное число. Сколько камне будет в кучке? '
    ))
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
        while nimcheck.niminput(stones, min(stones_total, 3)):
            stones = int(input(
                'Количество взятых камней должно быть положительным целым числом не больше {}. '
                'Сколько камней будете брать? '.format(min(stones_total, 3))
            ))
        count += 1
    stones_total -= stones
    print('Из кучки взято камней', stones)
    print('Осталось в кучке -', stones_total, '*' * stones_total)
    print()

if (-1) ** count < 0:
    print('Вы проиграли')
else:
    print('Вы выиграли!')
