"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    max_value = 101 # задаем максимальную границу поиска
    min_value = 0   # задаем минимальную границу поиска

    while True:
        
        count += 1
        predict_number = round((max_value + min_value) / 2)  # предполагаемое число среднее между границами поиска
        if predict_number > number:  #если предпологаемое число больше загаданного
            max_value = predict_number # тогда максимальная граница уменьшается до предпологаемого числа
        if predict_number < number:   #если предпологаемое число меньше загаданного
            min_value = predict_number  # тогда минимальная граница увеличивается до предпологаемого числа
        if number == predict_number:
            break  # выход из цикла если угадали
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score
score_game(random_predict)