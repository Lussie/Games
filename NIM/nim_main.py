import nimcheck
import NIM1
import NIM2
import NIM3

number_of_piles = int(input('Со сколькими кучками камней вы хотите сыграть? (от 1 до 3) '))

while nimcheck.niminput(number_of_piles, 3, 1):
    number_of_piles = int(input(
        'Количество кучек должно быть целым положительным числом от 1 до 3 включительно. Со сколькими кучками камней '
        'вы хотите сыграть? '
    ))

stones_total = []

for i in range(number_of_piles):
    stones_at_beginning = int(input('Сколько камней будет в кучке {}? '.format(i + 1)))
    while nimcheck.niminput(stones_at_beginning, stones_at_beginning):
        stones_at_beginning = int(input(
            'Можно вводить только целое положительное число. Сколько камне будет в кучке {}? '.format(i + 1)
        ))
    stones_total.append(stones_at_beginning)

# TODO: менять падеж у "кучек"

print('\nИтак, у вас', number_of_piles, 'кучки камней.')
for i in range(number_of_piles):
    print('В', i + 1, 'кучке -', stones_total[i], 'камней.')

result = None

if number_of_piles == 1:
    print('\nПравила:\nИгрок в свой ход берет из кучки от 1 до 3 камней. \nВыигрывает тот, кто возьмет последний '
          'камень.\n')
    result = NIM1.nim1(stones_total)
elif number_of_piles == 2:
    print('\nПравила: \nИгрок в свой ход берет любое количество камней из любой одной кучки. \nВыигрывает тот, кто '
          'возьмет последний камень.\n')
    result = NIM2.nim2(stones_total)
elif number_of_piles == 3:
    print('\nПравила: \nИгрок в свой ход берет любое количество камней из любой одной кучки. \nВыигрывает тот, '
          'кто возьмет последний камень.\n')
    result = NIM3.nim3(stones_total)

if result:
    print('Вы выиграли!')
else:
    print('Вы проиграли!')
