# модуль для общих функций для игр в ним

# проверка правильности ввода количества камней
def input(stones_input, max, min = 1):
    # print(stones_input)
    if stones_input < min or stones_input % 1 != 0 or stones_input > max:
        return 1
    else:
        return 0