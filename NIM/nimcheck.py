# модуль для общих функций для игр в ним

# проверка правильности ввода количества камней
def niminput(stones_input, stones_max, stones_min=1):
    if stones_input < stones_min or stones_input % 1 != 0 or stones_input > stones_max:
        return 1
    else:
        return 0
