import nimcheck


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
        number_of_piles = int(input(
            'Можно вводить только целое положительное число. Сколько камне будет в кучке {}? '.format(i + 1)
        ))
    stones_total.append(stones_at_beginning)

print(stones_total)
